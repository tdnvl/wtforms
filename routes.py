from flask import Flask, render_template, request, session, url_for, redirect
# from models import db, Contacts #import the db and the tables, too
# from forms import [list forms]

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


# Default port:
if __name__ == '__main__':
    app.run()