from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:root123@localhost/uki_school"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/")
def home():
    return "Flask + MySQL Connected"


if __name__ == "__main__":
    try:
        with app.app_context():
            db.session.execute(text("SELECT 1"))
            print("SUCCESS: Database Connected Successfully")

    except Exception as e:
        print("ERROR: Database Connection Failed")
        print(e)

    app.run(debug=True)
