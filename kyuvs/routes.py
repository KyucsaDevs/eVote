from kyuvs import app
from kyuvs import db,bcrypt
from flask import render_template,url_for,request,redirect,flash
from kyuvs.forms import LoginForm, PassresetForm, AdminLoginForm, PhotoForm, AddCandidate, RemoveCandidate,Vote
from kyuvs.models import Candidates, Students, SysUsers, Etokens #Voters
#from kyuvs.mail import Mails
from flask_login import login_user,current_user,logout_user,login_required
import time



#Student login function
@app.route("/", methods=['GET','POST'])
def login():
    form = LoginForm()
    student = Students()
    if current_user.is_authenticated:
       return redirect(url_for('user_dashboard'))
    if form.validate_on_submit():
        if form.username.data == '2100802718' and form.password.data == '2100802718':
            flash(f'First time login. An email with password reset token sent to {form.username.data}@std.kyu.ac.ug ','warning')
            return redirect(url_for('passreset'))
        else:
            if form.username.data == student.std_number and form.password.data == student.password:
                flash(f"Login successful!",'success')
                return redirect(url_for('user_dashboard'))
    return render_template('login.html',title='Student Login', form=form)


#Student password reset form function
@app.route("/resetpassword", methods=['GET','POST'])
def passreset():
    e_tokens = Etokens()
    form = PassresetForm()
    if form.validate_on_submit():
        if form.password.data == form.confirm_password.data and form.token.data == e_token.tokens:
            harshed_password = bcrypt(form.password.data)
            student = Students(password=harshed_password)
            flash (f"Password Reset successful!, Login with the new password.",'success')
            return redirect(url_for('login'))
        else:
            flash (f"Password doesn't match. Try again",'danger')
    return render_template('reset.html',title='Password Reset', form=form)


#Student's voting dashboard after successful login.
@app.route("/userdashboard")
#@login_required
def user_dashboard():
    return render_template('udashboard.html',title='User Dashboard')


#Admin Login Page
@app.route("/system", methods=['GET','POST'])
def admin_login():
    if current_user.is_authenticated:
       return redirect(url_for('admin_dashboard'))
    form = AdminLoginForm()
    if form.validate_on_submit():
        def validate_login(self,email,password):
            user = SysUsers.query.filter_by(email=form.email.data)
            if user and bcrypt.check_password_harsh(user.password, form.password.data):
                login_user(user)
                flash(f"Login successful!",'success')
                time.sleep(2)
                return redirect(url_for('admin_dashboard'))
            else:
                flash(f"Invalid Login! email or password is incorrect, Please try again.")
                return redirect(url_for(admin_login))


    return render_template('admin.html',title='Admin-Login',form = form)


#Admin Dashboard
@app.route("/dashboard", methods=['GET','POST'])
#@login_required
def admin_dashboard():
    form = PhotoForm()
    form1 = AddCandidate()
    form2 = RemoveCandidate()

#function for adding files to the database
    if form.validate_on_submit():
        users = Candidates(fullname=form1.fullname.data,regnumber=form1.regnumber.data,position=form1.position.data,
            slogan=form1.slogan.data,school=form1.school.data,course=form1.course.data,party=form1.party.data,avater=form1.avater.data)
        if form1.fullname.data not in users:
            db.session.add(users)
            db.session.commit()
            flash(f"Record added successfully. ",'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash(f"The Candidate already exists.",'info')
            return render_template('dashboard.html',title='Admin Dashboard', form=form, form1=form1,form2=form2)
#function to add candidate details to the database
    if form1.validate_on_submit():
        users_1 = Candidates(fullname=form1.fullname.data,regnumber=form1.regnumber.data,position=form1.position.data,
            slogan=form1.slogan.data,school=form1.school.data,course=form1.course.data,party=form1.party.data,avater=form1.avater.data)
        db.session.add(users_1)
        db.session.commit()
        flash(f"Record added successfully. ",'success')
        return redirect(url_for('admin_dashboard'))
    else:
        flash(f"Hurroy... Something happened Please try again.")
        return render_template('dashboard.html',title='Admin Dashboard', form=form, form1=form1,form2=form2)

#Function to check the record the user wants to delete from the database and delete
    if form2.validate_on_submit():
        users_2 = Candidates.query.filter_by(regnumber=form2.regnumber.data,position=form2.position.data)
        if user_2:
            db.session.delete(users_2)
            db.session.commit()
            flash(f"Candidates deleted successfully. ",'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash(f"Hurroy... Something went wrong, Please try again.")
            return render_template('dashboard.html',title='Admin Dashboard', form=form, form1=form1,form2=form2)
    return render_template('dashboard.html',title='Admin Dashboard', form=form, form1=form1,form2=form2)


#Poll Result
@app.route("/poll")
def poll_dashboard():
    return render_template('pollresult.html',title='Result View')


#logging user out of the system.
@app.route("/logout")
def logout():
    logout_user()
    flash(f"You are logout successfully.",'info')
    time.sleep(1)
    return redirect(url_for('admin_login'))