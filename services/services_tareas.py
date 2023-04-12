from config import database as _database
import sqlalchemy.orm as _orm
import fastapi as _fastapi
import fastapi.security as _security
import email_validator as _email_check
import models.tareas as _models
import schemas.schemas as _schemas
import passlib.hash as _hash
import jwt as _jwt


async def create_tarea(user: _schemas.User, db: _orm.Session, note: _schemas.NoteCreate):
    note = _models.Notes(**note.dict(), user_id=user.id)
    db.add(note)
    db.commit()
    db.refresh(note)
    return _schemas.Note.from_orm(note)

async def create_categoria(user: _schemas.User, db: _orm.Session, category: _schemas.CategoryCreate):
    category = _models.Category(**category.dict(), user_id=user.id)
    db.add(category)
    db.commit()
    db.refresh(category)
    return _schemas.Category.from_orm(category)

async  def get_user_note(user: _schemas.User, db: _orm.Session ):
    notes = db.query(_models.Notes).filter_by(user_id=user.id)

    return list(map(_schemas.Note.from_orm, notes))

async  def get_user_Category(user: _schemas.User, db: _orm.Session ):
    categorias = db.query(_models.Category).filter_by(user_id=user.id)

    return list(map(_schemas.Category.from_orm, categorias))
