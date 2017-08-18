from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_wtf import Form
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

"""@app.route('/')
def index():
	return render_template('index.html',
							current_time=datetime.utcnow())
"""

@app.route('/', methods=['GET', 'POST'])
def index():
	#name = None
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name')
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
		#form.name.data = ''
	return render_template('index.html', 
		form=form, name=session.get('name'))

	pass

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')


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






if __name__ == '__main__':
	manager.run()
	app.run(debug=True)
