from typing import List, Optional, Union

from pydantic import BaseModel, constr
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from database import Base

# 여기에서는 모델만 정의하기 때문에 세션 가져올 필요 없음. ######################################################################################################


class Ttable(Base):
    __tablename__ = "new_timetable"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    time = Column(Integer, nullable=False, default=0)
    day = Column(Integer, nullable=False)
    which_class = Column(
        String(1), nullable=False
    )  # String형식에는 길이를 필수로 지정해야함. #########################################################################################


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(
        String(64), nullable=False
    )  # 비밀번호는 SHA256으로 암호화했기 때문에 문자열 길이를 64이상으로 지정함. ##########################################################
    school_id = Column(String(10), nullable=False)


class Register_example(BaseModel):
    username: constr(min_length=6, max_length=30)
    school_id: str
    password: str
    re_pw: str

    # @validator("school_id")
    # def validate_department(cls, param):
    #     valid_departments = {'C', 'H', 'M'}  # 유효한 과의 첫 글자들
    #     if not param[0].upper() in valid_departments:  # 첫 글자를 대문자로 변환하여 확인
    #         raise ValueError("학번이 올바르지 않습니다.")
    #     return param


class Login_example(BaseModel):
    id: str
    pw: str
