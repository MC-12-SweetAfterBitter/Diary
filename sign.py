from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.makediary


# 메인 홈페이지 (HTML 화면 보여주기)
@app.route('/main')
def main():
    return render_template('main.html')


# 로그인 페이지
@app.route('/login')
def login():
    return render_template('login.html')


# 로그인 페이지
@app.route('/login', methods=['POST'])
def user_login():
    em_receive = request.form['em_give']
    pw_receive = request.form['pw_give']

    doc = {
        'em': em_receive,
        'pw': pw_receive
    }
    return render_template('login.html')


# 회원가입 페이지
@app.route('/signup')
def signup():
    return render_template('signup.html')


# 회원가입(POST) API
@app.route('/signup', methods=['POST'])
def user_infor():
    name_receive = request.form['name_give']
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']
    pwcf_receive = request.form['pwcf_give']

    doc = {
        'name':name_receive,
        'email':email_receive,
        'password':password_receive,
        'pwcf':pwcf_receive
    }
    db.userinfor.insert_one(doc)

    return jsonify({'ans':'success', 'msg': '가입완료'})


# 개인 다이어리 페이지
@app.route('/personal')
def personal():
    return render_template('personal_main.html')


# 글쓰기 페이지
@app.route('/write')
def write():
    return render_template('write.html')


# 주문 목록보기(Read) API
# @app.route('/login', methods=['GET'])
# def login_token():
#     d_user = list(db.diary.find({}, {'_id': False}))
#     return jsonify({'d_users': d_user})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)