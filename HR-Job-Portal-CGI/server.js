// server.js
const express = require('express');
const multer = require('multer');
const path = require('path');
const bodyParser = require('body-parser');
const { parseResume } = require('./resumeParser');
const { matchResume } = require('./matcher');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

// Serve HR input form
app.get('/', (req, res) => {
  res.sendFile(path.resolve(__dirname, 'public', 'hr_form.html'));
});

// Serve Candidate Application Form
app.get('/apply', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'apply_form.html'));
});

// Handle Job Requirements Submission
app.post('/submit-job', (req, res) => {
  const jobData = req.body;
  console.log('Job Data:', jobData);
  res.send('Job Requirements Submitted Successfully');
});

// Handle Candidate Resume Upload
app.post('/upload-resume', upload.single('resume'), async (req, res) => {
  if (!req.file) return res.status(400).send('No file uploaded.');
  const resumeData = await parseResume(req.file.path);
  console.log('Resume Data:', resumeData);

  // Perform Matching
  const jobData = {}; // Load job data for comparison (from DB or memory)
  const matchResult = matchResume(resumeData, jobData);

  res.json({ resumeData, matchResult });
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});