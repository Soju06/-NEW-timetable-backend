import jwt
import time
from datetime import datetime, timedelta

import hashlib

DAY = 86400
SECRET = "S@b4L"

def checkAuth(token):
    pass

def encToken(user_id):
  end = int(time()) + DAY
  tmp = {
    "id": user_id,
    "type": "auth",
    "role": "user",
    "end": end,
  }
  token = jwt.encode(tmp, SECRET, algorithm="HS256")
  return token

def hashing_pw(plain_pw):
    hashed_password = hashlib.sha256(plain_pw.encode('utf-8')).hexdigest()
    return hashed_password