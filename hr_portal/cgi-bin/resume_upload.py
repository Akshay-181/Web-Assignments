#!/usr/bin/env python3
import os
import json
from docx import Document
from pdfminer.high_level import extract_text

print("Content-type: text/html\n")

# Load job requirements
with open('../uploads/job_requirements.json') as f:
    job_data = json.load(f)

# Resume parsing
def parse_resume(file_path):
    _, ext = os.path.splitext(file_path)
    if ext == '.pdf':
        text = extract_text(file_path)
    elif ext in ['.doc', '.docx']:
        doc = Document(file_path)
        text = "\n".join([p.text for p in doc.paragraphs])
    else:
        return None
    return text

# Matching algorithm
def calculate_score(parsed_data, job_data):
    score = 0
    if any(skill.lower() in parsed_data.lower() for skill in job_data['skills']):
        score += 40
    if str(job_data['experience']) in parsed_data:
        score += 30
    if job_data['education'].lower() in parsed_data.lower():
        score += 30
    return score

# Process resumes in the upload directory
uploads_dir = "../uploads"
for filename in os.listdir(uploads_dir):
    if filename.endswith('.pdf') or filename.endswith('.docx'):
        resume_path = os.path.join(uploads_dir, filename)
        parsed_data = parse_resume(resume_path)
        
        if parsed_data:
            score = calculate_score(parsed_data, job_data)
            if score > 70:
                feedback = "Excellent match!"
            elif score > 50:
                feedback = "Good match, but consider improving some areas."
            else:
                feedback = "Weak match. Consider enhancing relevant skills."

            print(f"<h3>Resume: {filename} - Score: {score}%</h3>")
            print(f"<p>Feedback: {feedback}</p>")
