//Declaracion de Python-Shell
const {PythonShell} = require("python-shell");

//opciones enviadas a python
var options =
{
    mode: 'text', //como python recibira la informacion texto o binaria
    encoding: 'utf8', //codificacion de los datos
    pythonOptions: ['-u'], //obliga a las secuencias stdout y stderr a que no tengan búfer
    scriptPath: './', //la ubicacion donde se ecuentra el archivo a ejecutar
    args: ["romeo y julieta", "shakespeare"] //los argumentos que recibira python
};


var test = new PythonShell ('hello.py', options)
test.on('message', function(jsonFile)   //function, la manera de recibir la informacion que manda python como respuesta (return/print)
{

    var message = JSON.parse(jsonFile)
    console.log(message)     //Aqui podemos crear procesos con la informacion que manda de regreso


});