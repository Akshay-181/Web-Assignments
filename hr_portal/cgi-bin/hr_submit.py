#!/usr/bin/env python3
import cgi
import json

print("Content-type: text/html\n")

# Get form data
form = cgi.FieldStorage()
job_title = form.getvalue('job_title')
skills = form.getvalue('skills').split(',')
experience = int(form.getvalue('experience'))
education = form.getvalue('education')

# Validate criteria
if experience > 20 or "AI" in skills and experience < 2:
    print("<h3>Error: Impossible or contradictory criteria provided.</h3>")
else:
    # Save job requirements
    job_data = {
        "job_title": job_title,
        "skills": skills,
        "experience": experience,
        "education": education
    }
    with open('../uploads/job_requirements.json', 'w') as f:
        json.dump(job_data, f)

    print("<h3>Job requirements submitted successfully.</h3>")
