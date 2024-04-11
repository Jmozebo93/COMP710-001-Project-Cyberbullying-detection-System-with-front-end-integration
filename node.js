const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const path = require('path'); // Import the path module

const app = express();
const PORT = 3000;

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname))); // Update the path to serve static files

app.use(bodyParser.json());

app.post('/analyze', (req, res) => {
  const { tweet } = req.body;

  const pythonProcess = spawn('python', ['/workspaces/COMP710-001-Project-Cyberbullying-detection-System-with-front-end-integration/Model/Cyberbullying_Detection_System.py', tweet]);

  let result = '';

  pythonProcess.stdout.on('data', data => {
    result += data.toString();
  });

  pythonProcess.on('exit', code => {
    if (code === 0) {
      res.json({ result: result.trim() });
    } else {
      res.status(500).json({ error: 'Python script failed' });
    }
  });

  pythonProcess.on('error', err => {
    console.error('Python process error:', err);
    res.status(500).json({ error: 'Internal server error' });
  });
});

// Define a route handler for the root URL ("/") to serve the User_Interface.html file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname,'User_Interface.html'));
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

