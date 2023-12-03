from flask import Flask, render_template
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app = Flask(__name__)
# link for the database connection
# enter your address instead of this
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Sagar123&@localhost:3306/careers_website"
db.init_app(app)


class Opportunities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(12), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    salary = db.Column(db.Integer, nullable=False)


@app.route("/", methods=["GET"])
def home():
    jobs = Opportunities.query.all()
    return render_template('home.html', jobs=jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
