from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn
from sqlalchemy.exc import IntegrityError
from contextlib import asynccontextmanager

from base import get_session
from schemas import CreateSchedule, ReturnSchedule
from utils import create_intake_time_list, create_how_often_from_str
from CRUD import add_new_schedule, get_schedule_for_user, \
    get_all_schedules_for_user, get_next_takings_for_user
from scheduler import scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    yield
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)


@app.get(
    path='/schedule',
    summary='Возвращает данные о выбранном расписании с рассчитанным графиком приёмов на день'
)
async def root(
    user_id,
    schedule_id,
    session: AsyncSession = Depends(get_session)
):
    schedule: ReturnSchedule = await get_schedule_for_user(
        session, user_id,
        int(schedule_id)
    )
    return schedule


@app.post(
    path='/schedule',
    summary='Создает расписание'
)
async def create_schedule(
    schedule: CreateSchedule,
    session: AsyncSession = Depends(get_session)
):
    if type(schedule.how_often) is str:
        try:
            schedule.how_often = create_how_often_from_str(schedule.how_often)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Ошибка валидациии. Доступные текстовые значения: Ежечасно, Ежедневно"
            )

    intake_time_list = create_intake_time_list(schedule.how_often)
    data = schedule.model_dump()
    data['intake_time_list'] = intake_time_list
    schedule = add_new_schedule(session, data)
    try:
        await session.commit()
        return {'id': schedule.id}
    except IntegrityError:
        await session.rollback()
        raise Exception("Ошибка валидации данных")


@app.get(
    path='/schedules',
    summary='Возвращает данные о всех расписаниях пользователя'
)
async def get_schedules(user_id, session: AsyncSession = Depends(get_session)):
    result = await get_all_schedules_for_user(session, user_id)
    return result


@app.get(
    path='/next_taking',
    summary='Возвращает данные о всех расписаниях'
    'пользователя находящихся в промежутке между сейчас и NEXT_TAKING'
)
async def get_next_taking(user_id, session: AsyncSession = Depends(get_session)):
    result = await get_next_takings_for_user(session, user_id)
    return result


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
