from flask import Flask, render_template
from flask import request
from flask import redirect, url_for
from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)



'''@app.route('/')
def index():
	return '<h1>Hello World!</h1>'
@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' %name
	pass
@app.route('/useragent')
def browserUserAgent():
	user_agent = request.headers.get('User-Agent')
	return '<p> My browser is %s</p>' % user_agent
	pass
@app.route('/badrequest')
def badrequest():
	return '<h1>Bad request!</h1>', 400
	pass
@app.route('/redirect')
def redirec():
	return redirect('http://www.mioemi.com')
	pass'''

@app.route('/index')
def index():
	return render_template('index.html')
	pass






if __name__ == '__main__':
	manager.run()
	app.run(debug=True)
