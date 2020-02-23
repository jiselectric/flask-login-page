from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(128))
    def __init__(self, id, password):
        self.id = id
        self.password = password



# example data sets
USERS = {'jikim' : '1234'}

# Login Page
@app.route('/')
def index():
    return render_template('index.html')

# Account Check
@app.route('/check', methods=['POST'])
def check():
    id = request.form.get('id')
    pw = request.form.get('pw')

    if id in USERS and pw == USERS[id]:
        return 'correct'
    elif id in USERS and pw != USERS[id]:
        return 'wrongPW'
    else:
        return 'wrong'


# Login Successful
@app.route('/success')
def success():
    return render_template('success.html')

# Register Form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if register.method == 'POST':
        new_user = User(id=request.form['id'], password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('register.html')
    return render_template('register.html')

# Error Handler
app.run()