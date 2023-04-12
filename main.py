import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm

import models.tareas as _tareas
from config import database as _database
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.tareas import tareas_routes
_tareas._database.Base.metadata.create_all(bind=_database.engine)


app = _fastapi.FastAPI()
app.include_router(auth_routes, prefix="/api")
app.include_router(tareas_routes, prefix="/api")
app.title = "Api VozaVoz"
app.version = "0.0.1"

load_dotenv()
