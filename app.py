from flask import Flask, render_template, request

app = Flask(__name__)

# example data sets
USERS = {'jikim' : '1234'}

# Login Page
@app.route('/')
def index():
    return render_template('index.html')

# Login Successful
@app.route('/success')
def success():
    return render_template('success.html')

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

# Error Handler
app.run()