from datetime import datetime
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, constr

app = FastAPI()

from config import *
from database import *
from model import *
from tools import *

Base.metadata.create_all(
    bind=engine
)  # DB 구조 자동 생성 #############################################################################################


@app.get("/api/timetable")
async def timetable():
    time_format = {
        "08:10": 0,
        "08:40": 1,
        "09:40": 2,
        "10:40": 3,
        "11:40": 4,
        "12:30": 9,  # 점심시간은 9교시로 표시함
        "01:20": 5,
        "02:10": 6,
        "03:10": 7,
        "04:10": 8,  # 학교 끝~~~
    }

    now = datetime.now()
    clock = now.strftime("%H:%M")
    current_weekday = now.weekday()  # 0:월요일 , 6:일요일

    if current_weekday == 5 or current_weekday == 6:
        return {"오늘은 수업이 없습니다."}

    # 수업시간인지 확인
    for param in time_format:
        if clock >= int(time_format[param]):
            if clock < int(time_format[param]):
                current_time = param

    if not current_time:  # 만약 아니라면 반환
        return {"현재 수업 시간이 아닙니다."}

    # 뽑아온 시간을 통해 쿼리문으로 조회하기
    current_lecture = Ttable.query.filter(
        current_time, current_weekday
    )  # 유저기능으로 반에 맞는 시간표 구현할것.

    # db 모델 토대로 객체 생성
    timetable_data = []
    for item in current_lecture:
        timetable_data.append(
            {"id": item.id, "content": item.content, "time": item.time, "day": item.day}
        )

    return timetable_data  # 그냥 jsonify로 직렬화 (테스트)


@app.post("/api/register")
async def register(
    data: Register_example,
):  # , db: Session = Depends(get_db)): # DB 굳이 이렇게 받을 필요 없음. 받고싶으면 Depends(SessionLocal)로 받아도 됨. ########################################
    if data.password != data.re_pw:
        return {"비밀번호가 일치하지 않습니다."}

    hashed_pw = hashing_pw(
        data.password
    )  # SHA256은 64자리 문자열을 반환함. ################################################################################

    # new_user = User(
    #     username=data.username,
    #     password=hashed_pw,
    #     school_id=data.school_id
    # )

    db_user = User(  # DB 객체는 불편하더라도 이렇게 상기하면서 넣어야 휴먼에러가 적음. ##########################################################################
        username=data.username,
        password=hashed_pw,
        school_id=data.school_id,
    )

    with SessionLocal() as db:  # with문을 사용하면 자동으로 세션을 닫아줌. #####################################################################################
        db.add(db_user)  # 세션에 데이터 추가
        db.commit()

    return {"ok": "True"}


@app.post("/api/login")
async def login(data: Login_example):
    pw = data.pw
    hashed_pw = hashing_pw(pw)

    user = User.objects.filter(data.id, hashed_pw)

    if not user:
        return {"아이디 혹은 비밀번호가 다릅니다."}

    token = encToken(user.id)
    return ({"ok": "true"}, token)


# @app.route('/cal', methods=['POST', 'GET'])
# def cal():
#     pass

# @app.route('/todaysfortune', methods=['GET'])
# def todaytsfortune():
#     try:
#         with open("flask-server/fortune.txt", 'r') as file:
#             lines = file.readlines()
#             line_number = random.randint(1, len(lines))
#             if 0 < line_number <= len(lines):
#                 specific_line = lines[line_number - 1]
#                 return specific_line
#             else:
#                 return "해당 줄이 존재하지 않습니다."
#     except file_notfound:
#         return jsonify({"Message": "파일을 찾을 수 없습니다."})


# @app.post("/commiturval")
# async def commiturval():
#     data = request.json

#     new_timetable = Ttable(
#         content=data['content'],
#         time=data.get('time'),
#         day=data.get('day')
#     )

#     session.add(new_timetable)  # 새로운 데이터 추가
#     session.commit()  # 커밋

#     return {
#         "ok" : True
#     }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
