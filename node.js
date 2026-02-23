const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

app.post('/analyze', (req, res) => {
  const { tweet } = req.body;

  if (typeof tweet !== 'string' || tweet.trim().length === 0) {
    return res.status(400).json({ error: 'Invalid input: tweet must be a non-empty string' });
  }

  if (tweet.length > 10000) {
    return res.status(400).json({ error: 'Input too long' });
  }

  const pythonProcess = spawn('python', [
    '/workspaces/COMP710-001-Project-Cyberbullying-detection-System-with-front-end-integration/Model/Cyberbullying_Detection_System.py',
    tweet
  ]);

  let result = '';

  pythonProcess.stdout.on('data', data => {
    result += data.toString();
  });

  pythonProcess.on('exit', code => {
    if (code === 0) {
      const prediction = result.trim();
      console.log('Prediction:', prediction);  // Log the content of prediction
      if (prediction === 'Cyberbullying') {
        res.json({ result: 'Your comment was flagged as inappropriate.' });
      } else {
        // code to post the comment
        res.json({ result: 'Your comment was posted successfully.' });
      }
    } else {
      res.status(500).json({ error: 'Python script failed' });
    }
  });

  pythonProcess.on('error', err => {
    console.error('Python process error:', err);
    res.status(500).json({ error: 'Internal server error' });
  });
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'User_Interface.html'));
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

