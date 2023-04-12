from typing import List
import fastapi as _fastapi
import services.services as _services
import services.services_tareas as _services_tareas
import schemas.schemas as _schemas
import sqlalchemy.orm as _orm

tareas_routes = _fastapi.APIRouter()


@tareas_routes.post("/notes", tags=['Tareas'], response_model=_schemas.Note)
async def create_tarea(note: _schemas.NoteCreate, user: _schemas.User = _fastapi.Depends(_services.get_current_user),
                 db: _orm.Session = _fastapi.Depends(_services.get_db)) -> dict:
    return await _services_tareas.create_tarea(user=user,db=db,note=note)


@tareas_routes.post("/category", tags=['Tareas'], response_model=_schemas.Category)
async def create_categoria(category: _schemas.CategoryCreate, user: _schemas.User = _fastapi.Depends(_services.get_current_user),
                 db: _orm.Session = _fastapi.Depends(_services.get_db)) -> dict:
    return await _services_tareas.create_categoria(user=user,db=db,category=category)


@tareas_routes.get("/notes", tags=['Tareas'], response_model=List[_schemas.Note])
async def get_note(user:_schemas.User = _fastapi.Depends(_services.get_current_user),
                   db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services_tareas.get_user_note(user=user,db=db)


@tareas_routes.get("/categorys", tags=['Tareas'], response_model=List[_schemas.Category])
async def get_Categori(user:_schemas.User = _fastapi.Depends(_services.get_current_user),
                   db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services_tareas.get_user_Category(user=user, db=db)
