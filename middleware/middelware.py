import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

def createToken(id, expires_delta: timedelta = timedelta(hours=1)):
    tokenEncode = {"id": id}
    expire = datetime.utcnow() + expires_delta
    tokenEncode.update({"exp": expire})

    token = jwt.encode(tokenEncode, os.getenv("SECRET_KEY"), algorithm="HS256")

    return token

def getUserIdByToken(token):
    if token == None:
        return None

    try:
        tokenCheck = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None

    userId = tokenCheck.get("id")

    return userId