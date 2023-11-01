from flask import Flask, redirect, url_for, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return redirect(url_for('index'))

@app.route("/submit" , methods=["POST"])
def details():
	data = request.form.get('data')
	try:
		with open("....txt" , 'a') as wf:
			wf.writelines(f"{data}\n")
			pass
		return "<h1><i>Uploading Done</i></h1>"
	except:
		return redirect("/")

@app.route("/<name>")
def justname(name):
	if name.lower() == 'admin':
		return render_template('admin_panel.html')

	elif name.lower() == 'uploads':
		return render_template('uploads.html')

	else:
		return f'<h1>Hello {name}'

@app.route("/uploads" , methods=["POST"])
def upload():
	
	file = request.files['file']

	if file.filename == "":
		return "No selected file"

	if file:
		filename = os.path.join(app.config['UPLOAD_FOLDER'] , file.filename)
		file.save(filename)
		return '<h1>File uploaded successfully </h1>'

@app.route("/admin" , methods=["POST"])
def admin():
	name = request.form.get('content')
	password = request.form.get('content2')
	with open('....txt' , 'r') as rf1:
		data1 = rf1.readlines()
	with open('admin.md' , 'r') as rd:
		data = rd.readline().split(":")
		pass
	if name in data and password in data:
		return data1
	else:
		return redirect("/")

if __name__ == "__main__":
	app.run(debug=True , port=8080)