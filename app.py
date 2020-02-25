from flask import Flask, render_template, request
import pickle as pk
app = Flask(__name__)
try:
    f = open('user.db', 'rb')
    users = pk.load(f)
    f.close()
except:
    users = {}


# Login Page
@app.route('/')
def index():
    return render_template('index.html')

# Account Check
@app.route('/check', methods=['POST'])
def check():
    id = request.form.get('id')
    pw = request.form.get('pw')

    if id not in users:
        return 'Account Not Found!'
    elif users[id] != pw:
        return 'Password Not Match'
    else:
        return 'success'

# Login Successful
@app.route('/success')
def success():
    return render_template('success.html')

# Account Register
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/regist', methods=["POST"])
def regist():
    id = request.form.get("id")
    pw = request.form.get("pw")

    if id not in users:
        users[id] = pw
        f = open("user.db", "wb")
        pk.dump(users, f)
        f.close()
        return "Account Created"
    else:
        return "Account Already Exists"

# Error Handler
app.run()