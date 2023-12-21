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

def check_auth(token):
  unix_time = int(time())
  try:
    tmp = jwt.decode(token, SECRET, algorithms="HS256")
    if tmp["type"] == "auth" and tmp["end"] > unix_time:
      return tmp["id"]
    else:
      return False
  except:
    return False

def hashing_pw(plain_pw):
  
  salted_pw = plain_pw + SECRET

  hashed_password = hashlib.sha256(salted_pw.encode('utf-8')).hexdigest()
  return hashed_password
