//Declaracion de Python-Shell
const {PythonShell} = require("python-shell");

function pyMessage() //funcion llamda desde html
{
    message = document.getElementById("msg").value; //obtener valor de id=msg
    document.getElementById("msg").value = ""; //limpia el input msg

    //opciones que python requiere para correr el archivo de manera especifica
    var options =
    {
        mode: 'text', //como python recibira la informacion texto o binaria
        encoding: 'utf8', //codificacion de los datos
        pythonOptions: ['-u'], //obliga a las secuencias stdout y stderr a que no tengan búfer
        scriptPath: './Engines', //la ubicacion donde se ecuentra el archivo a ejecutar desde main.js
        args: [message] //los argumentos que recibira python
    };



    var test = new PythonShell ('message.py', options) //crea un objeto tipo python shel
    test.on('message', function(message)   //function, la manera de recibir la informacion que manda python como respuesta (return/print)
    {


        console.log(message)     //Aqui podemos crear procesos con la informacion que manda de regreso


    });
}
