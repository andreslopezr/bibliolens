//Declaracion de Python-Shell
const {PythonShell} = require("python-shell");

//opciones enviadas a python
var options =
{
    mode: 'text', //como python recibira la informacion texto o binaria
    encoding: 'utf8', //codificacion de los datos
    pythonOptions: ['-u'], //obliga a las secuencias stdout y stderr a que no tengan búfer
    scriptPath: './', //la ubicacion donde se ecuentra el archivo a ejecutar
    args: []
};


var test = new PythonShell ('image.py', options) //crea una instancia de python-shell
test.on('message', function(jsonFile)   //function, la manera de recibir la informacion que manda python como respuesta (return/print)
{

    var message = JSON.parse(jsonFile) //convierte un string(el cual envia python) a json
    console.log(message["imagen"])

});