const {PythonShell} = require("python-shell");


function addBook()
{  
    var id = document.getElementById("libro_id").value; 
    document.getElementById("libro_id").value = "";

    var titulo = document.getElementById("titulo").value;
    document.getElementById("titulo").value = "";

    var autor = document.getElementById("autor").value;
    document.getElementById("autor").value = "";

    var editorial = document.getElementById("editorial").value;
    document.getElementById("editorial").value = "";

    var genero = document.getElementById("genero").value;
    document.getElementById("genero").value = "";

    var options =
    {
        mode: 'text', 
        encoding: 'utf8', 
        pythonOptions: ['-u'], 
        scriptPath: './Engines/ORM',
        args: [id, titulo, autor, editorial, genero]
    };

    var pythonCall = new PythonShell("adding.py", options)
    pythonCall.on("message", function(message)
    {
        if (message=="error: duplicate primary keys")
            window.alert("Existe otro libro con el mismo id")
        else
            console.log(message)
    });
} 
