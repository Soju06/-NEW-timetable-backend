import jwt
import time
from datetime import datetime, timedelta

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