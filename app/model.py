from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from pydantic import BaseModel

from database import Base

from database import SessionLocal
db = SessionLocal()

class Ttable(Base):
    __tablename__ = "new_timetable"

    id = Column(Integer, primary_key=True, autoincrement=True),
    content = Column(Text, nullable=False),
    time = Column(Integer, nullable=False, default=0),
    day = Column(Integer, nullable=False),
    which_class = Column(String, nullable=False)
    
class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True),
    username = Column(String, nullable=False),
    password = Column(String, nullable=False)
    
# class Todo_example(BaseModel):
#     id = str

class User_example(BaseModel):
    id = str 
    school_num = str
    pw = str
    re_pw = str 
    auth_code = str