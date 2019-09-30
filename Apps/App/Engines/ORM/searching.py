from sqlalchemy.exc import IntegrityError
from nltk.corpus import stopwords
from connection import *
import sys
import json
titulo, autor, editorial, genero, color, prioridad = 1, 2, 3, 4, 5, 6, #referencia de index


global sesion
sesion = createDB() #con esta clase interactuamos con las tablas
arg = "aef fea fe efa feaw"

class Filter():
    libros = []
    titulo = ""
    autor = ""
    editorial = "" 
    genero = ""
    contenido_list = "" #varias palabras 
    contenido = "" #palabra clave 
    prioridad = ""
    nexos = set(stopwords.words('spanish')) #falta solucionar el error de no encontrar spanish
    

    def Titulo(self):
        self.libros = sesion.query(Libro.filter(Libro.titulo.contains(self.titulo))).all()
    
    def Autor(self):
        self.libros = sesion.query(Libro.filter(Libro.autor.contains(self.autor))).all()
    
    def Editorial(self):
        self.libros = sesion.query(Libro.filter(Libro.autor.contains(self.editorial))).all()

    def Genero(self):
        self.libros = sesion.query(Libro.filter(Libro.genero.contains(self.genero))).all()
    
    def Contenido(self):
        self.libros = sesion.query(Libro.filter(Libro.contenido.contains(self.contenido))).all()

    def normalizar(self, word):
        word = word.lower()
        word = word.lstrip(' ')
        word = word.rstrip(' ')
        word = word.replace('á', 'a')
        word = word.replace('é', 'e')
        word = word.replace('í', 'i')
        word = word.replace('ó', 'o')
        word = word.replace('ú', 'u')
        return word
    
    def Format(self):
        self.titulo = self.normalizar(self.titulo) #dando formato a titulo
        self.autor = self.normalizar(self.autor) #dando formato a autor
        self.editorial = self.normalizar(self.editorial) #dando formato a editorial
        self.genero = self.genero(self.genero) #dando formato a genero
        #dando formato a contenido_list
        new_words = []
        for palabra in self.contenido_list:
            if not palabra in self.nexos:
                palabra = palabra.lower()
                new_words.append(palabra)
        self.contenido_list = new_words















'''modificar los atributos de el objeto con argv'''
modelo = Filter()
modelo.titulo = ""
modelo.autor = ""
modelo.editorial = ""
modelo.genero = ""
modelo.contenido_list = arg.split()
modelo.prioridad = ""

modelo.Format() #damos formato al contenido

if modelo.prioridad == "titulo":
    modelo.Titulo()
if modelo.prioridad == "autor":
    modelo.Autor()
if modelo.prioridad == "editorial":
    modelo.Editorial()
if modelo.prioridad == "genero":
    modelo.Genero()
if modelo.prioridad == "contenido":
    for word in modelo.contenido_list:
        modelo.contenido = word
        modelo.Contenido()


if not modelo.titulo == "":
    modelo.Titulo()
if not modelo.autor == "":
    modelo.Autor()
if not modelo.editorial == "":
    modelo.Editorial()
if not modelo.genero == "":
    for word in modelo.contenido_list:
        modelo.contenido = word
        modelo.Contenido()


'''
Libro pertenece a la clase Libro
por lo tanto tiene mas atributos
de los que se buscan
por obvias razones estos atributos no se agregan al filtro  de busqueda



obtener los index mediante el argv enviado por js
el cual dira que parte de la lista devolver
devolver 10 en 10 libros

arg = 0         range(0, 10)
arg = 1         range(11, 21)
arg = 2         range(22, 32)
arg = 3         range(33, 43)

formula         range(arg*10+arg, arg*10+arg*10)
'''
arg = 1
a = arg * 10 + arg
b = a + 10


sesion.close()

json_file = []
for i in range(a, b):
    try:
        json_constructor = \
        {
            "titulo": f"{modelo.libros[i].titulo}",
            "autor": f"{modelo.libros[i].autor}",
            "editorial": f"{modelo.libros[i].editorial}",
            "genero": f"{modelo.libros[i].genero}",
            "contenido": f"{modelo.libros[i].contenido}",
            "portada": f"{modelo.libros[i].portada}"
        }
        model
        json_file.append(json_constructor)
    except IndexError:
        sesion.close()
        print(json.dumps(json_file))