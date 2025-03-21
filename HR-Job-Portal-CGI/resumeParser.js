
// resumeParser.js
const fs = require('fs');
const pdfParse = require('pdf-parse');
const WordExtractor = require('word-extractor');

async function parseResume(filePath) {
  const extension = path.extname(filePath);
  if (extension === '.pdf') {
    const dataBuffer = fs.readFileSync(filePath);
    const data = await pdfParse(dataBuffer);
    return { text: data.text };
  } else if (extension === '.docx') {
    const extractor = new WordExtractor();
    const extracted = await extractor.extract(filePath);
    return { text: extracted.getBody() };
  } else {
    throw new Error('Unsupported file format');
  }
}

module.exports = { parseResume };