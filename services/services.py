from config import database as _database
import sqlalchemy.orm as _orm
import fastapi as _fastapi
import fastapi.security as _security
import email_validator as _email_check
import passlib.hash as _hash
import jwt as _jwt
#
import models.tareas as _models
import schemas.schemas as _schemas

_JWT_SECRET = "secreto"
oauth2schema = _security.OAuth2PasswordBearer("/api/token")

def _create_database():
    return _database.Base.metadata.createall(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user(email: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.email == email).first()


async def create_User(user: _schemas.UserCreate, db=_orm.Session):
    # Chet email
    try:
        valid = _email_check.validate_email(email=user.email)

        email = valid.email
    except _email_check.EmailNotValidError:
        raise _fastapi.HTTPException(
            status_code=404, detail="Ingresa un Email valido"
        )
    hashed_password = _hash.bcrypt.hash(user.password)
    user_obj = _models.User(firstname=user.firstname, lastname=user.lastname, email=email,
                            hashed_password=hashed_password)

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


async def authenticate_user(email: str, password: str, db: _orm.Session):
    user = await get_user(email=email, db=db)

    if not user:
        return False
    if not user.verify_password(password=password):
        return False
    return user


async def get_current_user(db: _orm.Session = _fastapi.Depends(get_db), token: str = _fastapi.Depends(oauth2schema)):

    try:
        payload = _jwt.decode(token,_JWT_SECRET,algorithms=["HS256"])
        user = db.query(_models.User).get(payload["id"])
    except:
        raise _fastapi.HTTPException(
            status_code=401,detail="Email o contraseña incorrectos"
        )
    return _schemas.User.from_orm(user)
