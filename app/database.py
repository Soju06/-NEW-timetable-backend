from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:sojuKing@localhost:3306/timetable"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(
    bind=engine
)  # 기본값에 자동으로 커밋도 해주고, 자동으로 닫아줌. ###################################################################

Base = declarative_base()
