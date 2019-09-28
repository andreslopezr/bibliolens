from sqlalchemy.exc import IntegrityError
from connection import *
import sys
titulo, autor, editorial, genero, color, contenido, prioridad = 1, 2, 3, 4, 5, 6, 7 #referencia de index


sesion = createDB() #con esta clase interactuamos con las tablas

try:
    libro = Libro_row("", "", "", "", "", "", "") #constructor utilizar los argv
    sesion.add(libro) #añadimos a la base de datos
    sesion.commit() #guardamos la base de datos
except IntegrityError:
    print("error: duplicate primary keys") #error
finally:
    sesion.close()