from pydantic import BaseModel
from datetime import datetime


class CreateSchedule(BaseModel):

    name_of_pharmacy: str
    how_often: int | str
    end_at: datetime
    user_id: str


class ReturnSchedule(BaseModel):

    id: int
    name_of_pharmacy: str
    how_often: int
    end_at: datetime
    user_id: str
    intake_time_list: list
