#the default file to run with..$ python run.py in the command-line to start the server.

from kyuvs import app,db

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)