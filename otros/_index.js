// index.js
const { spawn } = require('child_process');

const proceso = spawn('py', ['./otros/prueba.py']);

proceso.stdout.on('data', (datos) => {
  console.log(`stdout: ${datos}`);
});

proceso.stderr.on('data', (datos) => {
  console.error(`stderr: ${datos}`);
});

proceso.on('close', (codigo) => {
  console.log(`El proceso hijo salió con el código ${codigo}`);
});