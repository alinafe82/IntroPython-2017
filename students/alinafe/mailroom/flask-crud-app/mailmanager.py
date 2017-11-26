import os
from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


#initialize flask application
app = Flask(__name__)

engine = create_engine('postgresql://postgres:postgres@localhost:5432/mailroom')
db = SQLAlchemy(app)


class Donor(db.Model):
    FirstName = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    LastName = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.FirstName)
        return "<Title: {}>".format(self.LastName)

# Routing
# Python decorator for Flask, mapping main part of application (/) to home() function
# Add methods=["GET", "POST"]) to our route decorator.
# By default, Flask accepts GET requests for all routes, so here we're telling it to allow GET and POST requests.
@app.route("/", methods=["GET", "POST"])
def home():
    #return a message on the basic wep page
    #return "My Mailroom app"

    #render the home page
    if request.form:
        print(request.form) #print to see if its working
    return render_template("home.html")

#Set debug output
if __name__ =="__main__":
    app.run(debug=True)
