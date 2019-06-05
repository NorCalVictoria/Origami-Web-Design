from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

	#return '<h1>GOT HERE</h1>'
	return render_template('index.html')

@app.route('/about.html')
def about():
	#return '<h1> Working </h1>'
	return render_template('about.html')

@app.route('/services.html', methods=['GET', 'POST'])
def services():
	return render_template('services.html')





if __name__ == '__main__' :
	app.run(host='0.0.0.0', debug=True )