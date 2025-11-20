const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');
const path = require('path');
let mainWindow;
let pythonProcess;
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });
  mainWindow.loadFile('src/ui/index.html');
  // Start Python backend
  pythonProcess = spawn('python', [path.join(__dirname, 'src/main.py')], {
    stdio: 'inherit',
  });
  pythonProcess.on('close', () => {
    console.log('Python backend closed');
  });
}
app.whenReady().then(createWindow);
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
  if (pythonProcess) pythonProcess.kill();
});
ipcMain.on('authenticate', (event, apiKey) => {
