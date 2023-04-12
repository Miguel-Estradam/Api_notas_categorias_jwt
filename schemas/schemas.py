import datetime as _dt
from pydantic import  BaseModel, Field

class _UserBase(BaseModel):

    email: str

class UserLogin(_UserBase):
    password: str

    class Config:
        orm_mode = True

class UserCreate(_UserBase):
    firstname: str
    lastname: str
    password: str

    class Config:
        orm_mode = True


class User(_UserBase):
    id: int
    firstname: str
    lastname: str
    date_created: _dt.datetime

    class Config:
        orm_mode = True

class _NotesBase(BaseModel):
    tittle: str = Field(default="Titulo de la tarea", min_length=1, max_length=200)
    encargado: str = Field(default="Encargado de la tarea", min_length=1, max_length=100)
    description: str = Field(default="Descripcion de la tarea", min_length=1, max_length=1000)
    horas: int
    date_finish: _dt.datetime


class NoteCreate(_NotesBase):

    category_id: int

    class Config:
        orm_mode = True
class Note(_NotesBase):
    id : int
    user_id : int
    category_id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


class _CategoryBase(BaseModel):
    tittle: str


class CategoryCreate(_CategoryBase):


    class Config:
        orm_mode = True

class Category(_CategoryBase):
    user_id: int
    date_created: _dt.datetime


    class Config:
        orm_mode = True