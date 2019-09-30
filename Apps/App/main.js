const {app, BrowserWindow} = require('electron') //importar electron

function createWindow () //crear ventana alto y ancho
{
    window = new BrowserWindow    //nueva ventana
    (
        {
            width: 1280, //ancho
            height: 720, //alto
            webPreferences: 
            {
                nodeIntegration: true,
            }
        }
    )
    window.loadFile('./Views/book_aggregator.html') //archivo a abrir
}







app.on('ready', createWindow)   //iniciar aplicacion

app.on('window-all-closed', () => 
{
    if (process.platform !== 'darwin') //si la ultima ventana fue cerrada
    {
      app.quit() //terminar aplicacion
    }
})
