from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:root123@localhost/uki_school"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)  # Auto-increment primary key
    name = db.Column(db.String(100), nullable=False)  # Required field
    age = db.Column(db.Integer, nullable=False)  # Required field
    email = db.Column(db.String(150), unique=True, nullable=False)  # Must be unique
    gpa = db.Column(db.Float, nullable=True)


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)  # Auto-increment primary key
    course_name = db.Column(db.String(200), nullable=False)  # Required field
    course_code = db.Column(
        db.String(20), unique=True, nullable=False
    )  # Must be unique
    credits = db.Column(db.Integer, nullable=False)  # Required field
    instructor = db.Column(db.String(100), nullable=True)  # Optional field


@app.route("/")
def home():
    return "Flask + MySQL Connected"


if __name__ == "__main__":
    try:
        with app.app_context():
            db.session.execute(text("SELECT 1"))
            print("SUCCESS: Database Connected Successfully")
            db.create_all()

    except Exception as e:
        print("ERROR: {e}")
        print(e)

    app.run(debug=True)
