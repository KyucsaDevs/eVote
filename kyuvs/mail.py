from kyuvs import db,login_manager
from flask_login import UserMixin
from flask_mail import Mail, Message

mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'youremail@gmail.com'
app.config['MAIL_PASSWORD'] = '***********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

def index():
	msg = Message('Hello',sender='youremail@gmail.com', recipients=['form.username.data '+' @std.kyu.ac.ug'])
	msg.body = '''
	Hello {{form.username.data}} an email with a verification token sent to your student
	email to change your password.
	'''
	mail.send(msg)
	return "verification email sent"


from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

mail = Mail(app)

@app.route('/')
def send_mail():
    msg = Message('Hello', sender='your_email@gmail.com', recipients=[f'recipient_email{fro.mail}@example.com'])
    msg.body = "Testing Flask-Mail"
    try:
        mail.send(msg)
        return "Mail sent!"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()

