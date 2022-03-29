from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.SweetAfterBitter

# 홈 화면 보여주기
@app.route('/')
def main():
    return render_template('main.html')

# 회원가입 화면 보여주기
@app.route('/signup')
def signup():
    return render_template('signup.html')

# 로그인 화면 보여주기
@app.route('/login')
def login():
    return render_template('login.html')

# 개인 일기장 보여주기
@app.route('/personal', methods=['GET','POST'])
def personal_main():
    return render_template('personal_main.html')

