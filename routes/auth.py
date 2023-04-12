from fastapi import APIRouter, Depends, HTTPException
from utils import functions_jwt as _funtions_jwt
import services.services as _services
import sqlalchemy.orm as _orm
import fastapi.security as _security
import fastapi as _fastapi
import schemas.schemas as _schemas

auth_routes = APIRouter()


#

@auth_routes.post("/token", tags=['Auth'])
async def generate_token(form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(),
                         db: _orm.Session = Depends(_services.get_db)):
    user = await _services.authenticate_user(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise _fastapi.HTTPException(status_code=401, detail="Credenciales incorrectas")
    return await _funtions_jwt.create_token(user=user)


@auth_routes.post("/users", tags=['Auth'])
async def createUser(user: _schemas.UserCreate, db: _orm.Session = Depends(_services.get_db)):
    print(user.dict())
    db_user = await _services.get_user(email=user.email, db=db)
    if db_user:
        raise HTTPException(
            status_code=400, detail="El usuario ya existe"
        )
    # Crear usuario
    user = await _services.create_User(user=user, db=db)
    # return token
    return await _funtions_jwt.create_token(user=user)


@auth_routes.get('/users/me', tags=['Auth'], response_model=_schemas.User)
async def get_user(user: _schemas.User = Depends(_services.get_current_user)):
    return user
