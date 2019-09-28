from connection import *
import sys
titulo, autor, editorial, genero, color, contenido, prioridad = 1, 2, 3, 4, 5, 6, 7 #referencia de index


sesion = createDB() #con esta clase interactuamos con las tablas

libro = sesion.query(Libro).filter(Libro.libro_id=="111-22").first() #obtiene un libro, filtrado por libro_id pasado por argv

libro = None #modificar los atributos

sesion.commit()