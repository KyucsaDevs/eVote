from kyuvs import db,login_manager
from flask_login import UserMixin

#User loader for managing the user session
@login_manager.user_loader
def load_user(user_id):
	return SysUsers.query.get(int(user_id))

#database for storing candidates details
class Candidates(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String(50), unique=True, nullable=False)
	regnumber = db.Column(db.String(30), unique=True, nullable=False)
	position = db.Column(db.String(40), unique=True, nullable=False)
	slogan = db.Column(db.String(50), unique=True, nullable=False)
	school = db.Column(db.String(30), unique=True, nullable=False)
	course = db.Column(db.String(30), unique=True, nullable=False)
	party = db.Column(db.String(10), unique=True, nullable=False)
	avater = db.Column(db.String(30), nullable=False, default="url_for('avater.png')")
	def __repr__(self):
		return f"Candidates('{self.fullname}','{self.regnumber}','{self.position}','{self.slogan}','{self.school}','{self.course}','{self.party}','{self.avater}')"


#database for storing student password reset tokens.
class Etokens(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	etoken = db.Column(db.String(6), unique=True, nullable=False)
	def __repr__(self):
		return f"Etokens('{self.etoken}')"

#database for storing students details.
class Students(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	std_number = db.Column(db.String(30), unique=True, nullable=False)
	password = db.Column(db.String(80), unique=True, nullable=False)

	def __repr__(self):
		return f"Students('{self.std_number}')"

#database for storing system votes.
#class Voters(db.Model):
#	id = db.Column(db.Integer, primary_key=True)
#	counter = db.Column(relationship=Candidates,db.Integer,nullable=True,Foreign_key=True)

#	def __repo__(self):
#		return f"Votes('{self.counters}')"


#database for storing system users details.
class SysUsers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	#username = db.Column(db.String(30), unique=True, nullable=False)
	email = db.Column(db.String(30), unique=True, nullable=False)
	password = db.Column(db.String(80), unique=True, nullable=False)

	def __repo__(self):
		return f"SysUsers('{self.username}','{self.email}')"
