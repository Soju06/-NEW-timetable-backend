from typing import Optional
from fastapi import FastAPI, Form, jsonify
from datetime import datetime

app = FastAPI()

from app.config import * 
from app.model import * 
from app.database import *
from app.tools import *


@app.get("/api/timetable")
async def timetable():
        time_format = {
        "08:10": 0,
        "08:40": 1,
        "09:40": 2,
        "10:40": 3,
        "11:40": 4,
        "12:40": 9, # 점심시간은 9교시로 표시함
        "01:20": 5,
        "02:10": 6,
        "03:10": 7,
        "04:10": 8, # 학교 끝~~~
        }

        now = datetime.now()
        clock = now.strftime("%H:%M")
        current_weekday = now.weekday() # 0:월요일 , 6:일요일
        
        if current_weekday == 5 or current_weekday == 6:
            return jsonify("오늘은 수업이 없습니다.")
        
        # 수업시간인지 확인
        for param in time_format:
            if clock >= time_format[param]:
                if clock < time_format[param]:
                    current_time = param
                    return jsonify(current_time)
        if not current_time: # 만약 아니라면 반환
            return jsonify("현재 수업 시간이 아닙니다.")
            
        # 뽑아온 시간을 통해 쿼리문으로 조회하기
        current_lecture = Ttable.query.filter(current_time, current_weekday).all() # 유저기능으로 반에 맞는 시간표 구현할것.

        # db 모델 토대로 객체 생성
        timetable_data = []
        for item in current_lecture:
            timetable_data.append({
                "id": item.id,
                "content": item.content,
                "time": item.time,
                "day": item.day
            })
        # 직렬화 하기 귀찮다
        return jsonify(timetable_data)
    
@app.post("/api/register")
async def register(data : User_example):
    
    if data.pw != data.re_pw:
        return jsonify({"비밀번호가 일치하지 않습니다."})
    
    hashed_pw = hashing_pw(data.pw)
    
    new_user = User(
        id=data.get('id'), 
        pw=data.get('hashed_pw'),
        school_id=data.get('day')
    )
    
    # jwt 추가 예정
    
    db.add(new_user)
    db.commit()
    

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
#     except FileNotFoundError:
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

# if __name__ == "__main__":
#     app.run(debug = True)