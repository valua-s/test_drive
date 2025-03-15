DAY_START_STR = '8:00'
DAY_END_STR = '22:00'


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


DAY_HOURS, DAY_START, DAY_END = day_hours_count(DAY_START_STR, DAY_END_STR)

NEXT_TAKING_PERIOD_STR = '1:00'
