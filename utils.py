import math
from constants import *    
from datetime import datetime, timedelta


def create_intake_time_list(how_often) -> list[datetime.time]:
    
    duration_inteval = DAY_HOURS / (how_often + 1)
    intake_time_list = []
    time_intake = DAY_START
    while time_intake + duration_inteval < DAY_END:
        time_intake += duration_inteval
        frac, whole = math.modf(time_intake)
        if frac > 0 and frac <= 0.25:
            frac = 15
        elif frac > 0.25 and frac <= 0.5:
            frac = 30
        elif frac > 0.50 and frac <= 0.75:
            frac = 45
        else:
            frac = '00'
            whole += 1
        intake_time_list.append(datetime.strptime(f'{int(whole)}:{frac}', "%H:%M").time())
    return intake_time_list


def get_now_and_delta_time() -> list[datetime.time]:

    now = datetime.now()
    time2 = datetime.strptime(NEXT_TAKING_PERIOD_STR, '%H:%M').time()
    delta = now + timedelta(hours=time2.hour, minutes=time2.minute)
    return now.time(), delta.time()


def create_how_often_from_str(s: str) -> int:

    if s == 'Ежечасно':
        return DAY_HOURS
    if s == 'Ежедневно':
        return 1
    else:
        raise Exception


def day_hours_count(DAY_START_STR, DAY_END_STR) -> int:

    start_hour, start_minutes = list(map(int, DAY_START_STR.split(':')))
    end_hour, end_minutes = list(map(int, DAY_END_STR.split(':')))
    if end_hour == 0:
        end_hour = 24
    if end_minutes % 15:
        end_minutes = (end_minutes // 15 + 1) // 4
    if start_minutes % 15:
        start_minutes = (start_minutes // 15 + 1) // 4
    DAY_START = start_hour + start_minutes
    DAY_END = end_hour + end_minutes
    return (
        DAY_END - DAY_START,
        DAY_START,
        DAY_END,
    )
