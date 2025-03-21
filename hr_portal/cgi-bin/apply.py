#!/usr/bin/env python3
import cgi
import os

print("Content-type: text/html\n")

# Get form data
form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
qualification = form.getvalue('qualification')
file_item = form['resume']

# Save resume
if file_item.filename:
    file_name = os.path.basename(file_item.filename)
    upload_path = f"../uploads/{file_name}"
    
    with open(upload_path, 'wb') as f:
        f.write(file_item.file.read())

    print(f"<h3>Application received. Resume uploaded successfully.</h3>")
else:
    print("<h3>Error: Resume not uploaded!</h3>")
