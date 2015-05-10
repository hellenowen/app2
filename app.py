from flask import Flask,render_template,session,request
# pyfirmata import Arduino,util
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms.fields import StringField,SubmitField
from wtforms.validators import Required

app=Flask(__name__)
bootstrap=Bootstrap(app)

class NameForm(Form):
	led=StringField('Which LED do you want to light on',validators=[Required()])
	submit=SubmitField('Light it')

@app.route('/',methods=['GET','POST'])
def index():
	form=NameForm()
	if form.validate_on_submit():
		#session['led']=form.led.data
		#return redirect(url_for('index'))
		#led=form.led.data
		led=1
	#return render_template('index.html',form=form,led=session.get('led'))
		return render_template('index.html',form=form,led=led)
	return render_template('index.html',form=form)
	
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404
	
@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'),500
	
if __name__=="__main__":
	app.run()
