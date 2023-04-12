from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse
import models.tareas as _models
import schemas.schemas as _schemas
import jwt as _jwt


def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date


async def create_token(user: _models.User):
    user_schema_obj = _schemas.User.from_orm(user)
    user_dict = user_schema_obj.dict()
    del user_dict["date_created"]

    token = _jwt.encode(payload={**user_dict,"exp": expire_date(2)}, key=getenv("SECRET"), algorithm="HS256")
    return dict(access_token=token, token_type="bearer")


def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2)}, key=getenv("SECRET"), algorithm="HS256")
    return token


def validate_token(token, output=False):
    try:
        if output:
            _jwt.decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        _jwt.decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except _jwt.exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except _jwt.exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)
