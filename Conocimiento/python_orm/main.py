from conexion import *


sesion = createDB() #con esta clase interactuamos con las tablas


#creamos un objeto de tipo libro
libro = Libro_row("111-22", "rom y julieta", "william shakespeare", "editorial universitaria", "drama", "rojo azul, verde, beige", "Romeo y Julieta William Shakespeare PlanetaLibronet Personajes Prólogo Acto primero Escena I Escena II Escena III Escena IV Escena V Acto segundo Escena I Escena II Escena III Escena IV Escena V Escena VI Acto tercero Escena I Escena II Escena III Escena IV Escena V Acto IV Escena I Escena II Escena III Escena IV Escena V Acto V Escena I Escena II Escena III FIN", "./portada.png")

sesion.add(libro) #añade el objeto a la DB
sesion.commit()#elimina el registro en la tabla
input() #pausa para checar los cambios en la DB

libro = sesion.query(Libro).filter(Libro.libro_id=="111-22").first() #obtiene un libro, filtrado por libro_id

libro.titulo = "romeo y julieta" #modificamos el objeto(libro)
sesion.commit() #salva los cambios en la DB
input() #pausa para checar los cambios en la DB


libro = sesion.query(Libro).filter(Libro.libro_id=="111-22").first() #obtiene un libro, filtrado por libro_id
sesion.delete(libro) #elimina el registro en la tabla
sesion.commit() #salva los cambios en la DB

#sesion.rollback() #deshace los cambios antes del commit

sesion.close() #cierra la conexion





