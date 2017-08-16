from flask import Flask, render_template
from flask import request
from flask import redirect, url_for
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from datetime import datetime
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

manager = Manager(app)

moment = Moment(app)



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

"""@app.route('/index')
def index():
	return render_template('index.html', current_time=datetime.utcnow())
	pass"""

@app.route('/')
def index():
	return render_template('index.html',
							current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)
	pass

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500


class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')



if __name__ == '__main__':
	manager.run()
	app.run(debug=True)
