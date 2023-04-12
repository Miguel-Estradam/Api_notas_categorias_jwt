import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
#DATABASE_URL = "mysql+mysqlconnector://root:@localhost/vozavoz_api"
DATABASE_URL = ("mysql+mysqlconnector://{user}:{password}@{host}/{database}".format(
    user="root",
    password="",
    host="localhost",
    database="vozavoz_api"
))

engine = _sql.create_engine(DATABASE_URL, echo=True)
SessionLocal = _orm.sessionmaker(bind=engine)
Base = _declarative.declarative_base()

