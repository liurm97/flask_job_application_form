from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

# initialize flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

# connect to the ninja database in local database
DATABASE_URI='mysql+mysqlconnector://root:970603LLF@localhost/ninja'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



# Create mysql table
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    available_date = db.Column(db.Date)
    employment_status = db.Column(db.String(50))

@app.route("/")
def renderHome():
    return render_template("index.html")

@app.route("/submit_application",methods=["POST"])
def submit_application():
    print(request.form)
    first_name = request.form['fname']
    last_name = request.form['lname']
    email = request.form['email']
    availability_date = request.form['date']
    employment_status = request.form['employment']

    form = Form(first_name=first_name,last_name=last_name,email=email,
                available_date=availability_date,employment_status=employment_status)
    # insert data into database
    db.session.add(form)
    db.session.commit()
    return "Successful!"

    # keys = [k for k,v in data.items()]
    # values = [v for k,v in data.items()]
    # # for k,v in data.items():
    # #     print(f"{k}: {v}")
    # return (f"<h1>Keys: </h1> <p>{[k for k in keys]}</p>"
    #         f"<h1>Values: </h1> <p>{[v for v in values]}</p>")

# run flask at port = 8080
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=8080)