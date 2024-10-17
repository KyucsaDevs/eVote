from flask import Flask
from datetime import datetime
from werkzeug.utils import secure_filename
import os,time, datetime
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user

# app initialisation
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kyuvs.db'
app.config['SECRET_KEY'] = '3ff3771f706de1c669ba4286d526f31f'
WTF_CSRF_SECRET_KEY = '3ff3771f706de1c669ba4286d526f31f'
db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'admin_dashboard','user_dashboard'
login_manager.login_message_category = 'info'

from kyuvs import routes