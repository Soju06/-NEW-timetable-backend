import jwt
import time
from datetime import datetime, timedelta

import hashlib

DAY = 86400
SECRET = "S@b4L"

chemical_condiment = "H4...IDONTKNOWWHYIBEFACEDTHISERROR"
salt = "hello.."

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
    return hashlib.sha256((plain_pw + salt).encode('utf-8')).hexdigest()

