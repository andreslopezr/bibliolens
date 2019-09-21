import json5 as json


#informacion en tipo JSON
data_py = \
{
    "Nombre": "Luis", #string
    "Apellido": "Lopez", #string
    "Edad": 17, #int
    "Hijos": #array
    [
        "Andres", #string
        "Carlos", #string
        "Fernando" #string
    ],
    "Trabaja": True, #bool
    "Trabajo": #dictionary
    {
        "Puesto": "Programador", #string
        "Antiguedad": 5 #int
    }
}


"""
de Python a JSON
"""
data_json = json.dumps(data_py)


#enviar data_json a js




"""
de JSON a Python"""


data_py = json.loads(data_json)




print(data_py["Nombre"]) #accediendo a un campo