from sqlalchemy.exc import IntegrityError
from connection import *
import sys
libro_id, titulo, autor, editorial, genero, contenido = 1, 2, 3, 4, 5, 6 #referencia de index

sesion = createDB() #con esta clase interactuamos con las tablas

try:
    libro = Libro_row \
    (
        sys.argv[libro_id], 
        sys.argv[titulo],
        sys.argv[autor],
        sys.argv[editorial],
        sys.argv[genero],
        "",
        ""
    )


    sesion.add(libro) #añadimos a la base de datos
    sesion.commit() #guardamos la base de datos
    print("libro nuevo")
except IntegrityError:
    print("error: duplicate primary keys") #error
finally:
    sesion.close()