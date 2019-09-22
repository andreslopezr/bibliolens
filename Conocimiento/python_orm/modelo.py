#aqui van los modelos de las bases de datos
import sqlalchemy as SQL #importamos sqlalchemy
import sqlalchemy.ext.declarative as model #importamos el modelo para las tablas
from sqlalchemy import Integer, String, Float, Boolean, Date, SmallInteger, Numeric, DateTime, Binary, Unicode, PickleType  #importamos los tipos de datos de las tablas

Base = model.declarative_base() #creamos la base para crear las clases(tablas)


#crear una archivo y una clase por cada tabla que deseemos
class Libro(Base): #heredamos de el modelo base
    __tablename__ = "Libro" #nombre de la tabla
    '''Atributos de la tabla'''
    libro_id = SQL.Column(String(10), primary_key=True)
    titulo = SQL.Column(String(50))
    autor = SQL.Column(String(50))
    editorial = SQL.Column(String(50))
    genero = SQL.Column(String(50))
    color = SQL.Column(String(50))
    contenido = SQL.Column(String(50))
    portada = SQL.Column(String(50))


#creamos la copia de la anterior clase, para usar un constructor, para añadir a la DB
class Libro_row(Libro):
    def __init__(self, libro_id, titulo, autor, editorial, genero, color, contenido, portada):
        self.libro_id = libro_id 
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.genero = genero
        self.color = color
        self.contenido = contenido
        self.portada = portada
