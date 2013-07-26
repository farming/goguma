from flask import render_template
from goguma import goguma

@goguma.route('/')
def index():
	return render_template('index.html')
