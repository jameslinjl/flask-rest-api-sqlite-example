from app import app
from flask import render_template

@app.route('/', methods=['GET'])
def base_view():
	return render_template('home.html')
