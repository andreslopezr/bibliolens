import sqlalchemy as SQL #importamos nuestra orm
import sqlalchemy.orm.session as orm_connect #importamos el modulo para modificar la tabla

from modelo import * #importamos los modelos
#...

#indicamos que sql utizaremos y la ubicacion de este
def createDB():
    engine = SQL.create_engine("sqlite:///database.db") #en este caso utilizaremos sqlite y estara alojada de manera local
    Base.metadata.create_all(engine) #crea la base de datos, en caso de no existir
    Sesion = orm_connect.sessionmaker(bind=engine) #nos traemos la clases para hacer la conexion
    return Sesion() #retornamos la clase para poder realizar la conexion y la interaccion


