//informacion en tipo JSON
dataJson = 
{
    "Nombre": "Luis", //string
    "Apellido": "Lopez", //string
    "Edad": 17, //int
    "Hijos": //array
    [
        "Andres", //string
        "Carlos", //string
        "Fernando" //string
    ],
    "Trabaja": true, //bool
    "Trabajo": //dictionary
    {
        "Puesto": "Programador", //string
        "Antiguedad": 5 //int
    }

}

console.log(dataJson) //imprime todo json

console.log(dataJson["Nombre"]) //imprime un campo de json

console.log(dataJson["Hijos"][0]) //imprime una posicion del arreglo

console.log(dataJson["Trabajo"]["Puesto"]) //imprime una definicion del diccionario



