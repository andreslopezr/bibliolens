import sqlalchemy as SQL
import sqlalchemy.orm.session as SQL_connect
from model import *


def createDB():
    engine = SQL.create_engine("sqlite:///Database/libros.db")
    Base.metadata.create_all(engine)
    Sesion = SQL_connect.sessionmaker(bind=engine)
    return Sesion()
    