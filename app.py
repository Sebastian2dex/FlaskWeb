from flask import Flask, redirect, url_for, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return redirect(url_for('index'))

@app.route("/submit", methods=["POST"])
def details():
    data = request.form.get('data')
    try:
        with open("data.txt", 'a') as wf:
            wf.write(f"{data}\n")
        return "<h1><i>Uploading Done</i></h1>"
    except Exception as e:
        # print(e)
        return redirect("/")

@app.route("/<name>")
def justname(name):
    if name.lower() == 'admin':
        return render_template('admin_panel.html')

    elif name.lower() == 'uploads':
        return render_template('uploads.html')

    else:
        return redirect('/')

@app.route("/uploads", methods=["POST"])
def upload():
    file = request.files['file']

    if not file or file.filename == "":
        return "No file selected"

    filename = os.path.join(app.config['UPLOAD_FOLDER'], str(file.filename))
    file.save(filename)
    return '<h1>File uploaded successfully</h1>'

@app.route("/admin", methods=["POST"])
def admin():
    name = request.form.get('content')
    password = request.form.get('content2')

    # Read submitted data
    try:
        with open('data.txt', 'r') as rf1:
            submitted_data = rf1.readlines()
    except FileNotFoundError:
        submitted_data = []

    # Read admin credentials from admin.md (example format: username:password) for simplicity
    try:
        with open('admin.md', 'r') as rd:
            username, pwd = rd.readline().strip().split(":")
    except Exception:
        return "<h3>Error: admin.md not configured properly</h3>"

    if name == username and password == pwd:
        return "<br>".join(submitted_data)
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=8080)

