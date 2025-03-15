from sqlalchemy import Column, Integer, String, DateTime, ARRAY, Time
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Schedule(Base):

    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    name_of_pharmacy = Column(String)
    how_often = Column(Integer, nullable=True)
    end_at = Column(DateTime(timezone=True))
    user_id = Column(String, index=True)
    intake_time_list = Column(ARRAY(Time))
