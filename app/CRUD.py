from sqlalchemy import select, delete

from utils import get_now_and_delta_time, datetime
from models import Schedule
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from constants import *


def add_new_schedule(session: AsyncSession, data: dict):
    new_schedule = Schedule(**data)
    session.add(new_schedule)
    return new_schedule


async def get_schedule_for_user(session: AsyncSession, user_id, schedule_id) -> Schedule:
    result = await session.execute(
        select(Schedule).where(
            Schedule.id == schedule_id,
            Schedule.user_id == user_id,
            Schedule.end_at > datetime.now()
            )
        )
    return result.scalar_one()


async def get_all_schedules_for_user(session: AsyncSession, user_id) -> list[Schedule]:
    result = await session.execute(
        select(Schedule).where(
            Schedule.user_id == user_id,
            Schedule.end_at > datetime.now()
            )
        )
    return result.scalars().all()


async def get_next_takings_for_user(session: AsyncSession, user_id) -> list[Schedule]:
    result = await session.execute(
        select(Schedule).where(
            Schedule.user_id == user_id,
            Schedule.end_at > datetime.now()
            )
        )
    now, delta = get_now_and_delta_time()

    all_pharmacy = result.scalars().all()
    next_taking_list = []
    for pharmacy in all_pharmacy:
        for time in pharmacy.intake_time_list:
            if time >= now and time <= delta:
                next_taking_list.append(pharmacy)
    return next_taking_list


def delete_old_schedules(session: Session):
    current_time = datetime.now()
    stmt = delete(Schedule).where(Schedule.end_at < current_time)
    session.execute(stmt)
    session.commit()
