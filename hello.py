from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<b>Welcome to Flask1212</b>'
@app.route('home')  
def home():  
    return 'my home page' 