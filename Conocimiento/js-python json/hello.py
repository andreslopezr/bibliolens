import sys
import json

titulo, autor, editorial, genero, color, contenido, prioridad = 1, 2, 3, 4, 5, 6, 7 #referencia de index

'''crear busquedas con los argumentos enviado por js'''
sys.argv[titulo]
sys.argv[autor]
sys.argv[genero]
sys.argv[contenido]


'''Con la busqueda recuperar consultas de sql'''
Titulo = "la excelente y lamentable tragedia de romeo y julieta"
Autor = " william shakespeare"
Editorial = "editorial universitaria"
Genero = "tragedia"
Color = "rojo-azul-blanco-beige"
Contenido = "Romeo y Julieta William Shakespeare PlanetaLibronet Personajes Prólogo Acto primero Escena I Escena II Escena III Escena IV Escena V Acto segundo Escena I Escena II Escena III Escena IV Escena V Escena VI Acto tercero Escena I Escena II Escena III Escena IV Escena V Acto IV Escena I Escena II Escena III Escena IV Escena V Acto V Escena I Escena II Escena III FIN"
Portada = "portada.jpg"

'''contruir un diccionario'''
json_constructor = \
{
    "titulo": f"{Titulo}",
    "autor": f"{Autor}",
    "editorial": f"{Editorial}",
    "genero": f"{Genero}",
    "color": f"{Color}",
    "contenido": f"{Contenido}",
    "portada": f"{Portada}"
}

libros = [json_constructor, json_constructor, json_constructor] #podemos crear multiples json en una lista
print(json.dumps(libros)) #convertir el diccionario a json file y enviarlo a js, si es lista creara varios json en uno solo
