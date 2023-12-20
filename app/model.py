from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from pydantic import BaseModel

from database import Base

class Ttable(Base):
    __tablename__ = "new_timetable"

    id = Column(Integer, primary_key=True, autoincrement=True),
    content = Column(Text, nullable=False),
    time = Column(Integer, nullable=False, default=0),
    day = Column(Integer, nullable=False),
    
# class Todo_example(BaseModel):
#     id = str
    