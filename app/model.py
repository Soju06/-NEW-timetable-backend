from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from pydantic import BaseModel, validator

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
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True),
    username = Column(String, nullable=False),
    password = Column(String, nullable=False)
    
# class Todo_example(BaseModel):
#     id = str

class User_example(BaseModel):
    id = str 
    school_id = str
    pw = str
    re_pw = str 
    
    @validator("school_id")
    def validate_department(cls, param):
        valid_departments = {'C', 'H', 'M'}  # 유효한 과의 첫 글자들
        if not param[0].upper() in valid_departments:  # 첫 글자를 대문자로 변환하여 확인
            raise ValueError("학번의 첫 글자는 C, H, M 중 하나여야 합니다.")
        return param