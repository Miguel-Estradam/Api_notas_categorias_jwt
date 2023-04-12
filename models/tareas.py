import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from config import database as _database

import passlib.hash as _hash

class User(_database.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer,primary_key=True, index=True)
    firstname = _sql.Column(_sql.String(100), index=True)
    lastname = _sql.Column(_sql.String(100), index=True)
    email = _sql.Column(_sql.String(200), unique=True, index=True)
    hashed_password = _sql.Column(_sql.String(5000))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow())

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password,self.hashed_password)

class Category(_database.Base):
    __tablename__ = 'categorys'
    id = _sql.Column(_sql.Integer,primary_key=True, index=True)
    tittle = _sql.Column(_sql.String(200),unique=True)
    user_id = _sql.Column(_sql.Integer, _sql.ForeignKey('users.id'),index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow())

    user = _orm.relationship(
        User, backref=_orm.backref('categorys', uselist=True))


class Notes(_database.Base):
    __tablename__ = "notes"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    tittle = _sql.Column(_sql.String(200))
    description = _sql.Column(_sql.String(1000))
    user_id = _sql.Column(_sql.Integer, _sql.ForeignKey('users.id'), index=True)
    category_id = _sql.Column(_sql.Integer, _sql.ForeignKey('categorys.id'), index=True)
    encargado = _sql.Column(_sql.String(100))
    horas = _sql.Column(_sql.Integer)
    date_finish = _sql.Column(_sql.DateTime)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow())

    categorys = _orm.relationship(
        Category, backref=_orm.backref('notes', uselist=True))
    user = _orm.relationship(
        User, backref=_orm.backref('notes', uselist=True))
