const {app, BrowserWindow} = require('electron') //importar electron

function createWindow () //crear ventana alto y ancho
{
    window = new BrowserWindow    //nueva ventana
    (
        {
            width: 800, //ancho
            height: 600 //alto
        }
    )
    window.loadFile('./Views/index.html') //archivo a abrir
}







app.on('ready', createWindow)   //iniciar aplicacion

app.on('window-all-closed', () => 
{
    if (process.platform !== 'darwin') //si la ultima ventana fue cerrada
    {
      app.quit() //terminar aplicacion
    }
})
