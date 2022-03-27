from flask import Flask, render_template, jsonify, request, session, redirect, url_for, escape
from datetime import timedelta
app = Flask(__name__)

from pymongo import MongoClient
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbhomework

app.secret_key = 'secretkey'  # secret_key는 서버상에 동작하는 어플리케이션 구분하기 위해 사용하고 복잡하게 만들어야 합니다.
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=1) # 로그인 지속시간을 정합니다. 현재 1분


# 회원가입 화면
@app.route('/')
def register_page():
    return render_template('register.html')
# 로그인 화면
@app.route('/login')
def login_page():
    if "name" in session:
        return jsonify({"ans":"success"},{"msg" : "환영합니다 {}님".format(escape(session['name']))})
    return render_template('login.html')


# 회원가입(POST) API
@app.route('/register', methods=['POST'])
def resgister():
    name_receive = request.form['name_give']
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']
    pwcf_receive = request.form['pwcf_give']
    print(name_receive,email_receive,password_receive,pwcf_receive)

    res = db.diary.find({}, {'_id': False})


    for list in res:
        # 공백 처리, 해당 부분에서 약간의 오류를 발생시키면 html 스크립트 공백체크가 작동한다..
        if name_receive == '' or email_receive == '' or password_receive == '' or  pwcf_receive == '':
            return jsonify({'ans': 'fail', 'msg': '공백이 있습니다'})
        # 회원가입 시 중복 ID, Email 처리
        elif list['name'] == name_receive or list['email'] == email_receive:
            return jsonify({'ans': 'fail', 'msg': '아이디 또는 이메일 중복!'})
        # 2차 비밀번호 체크
        elif pwcf_receive != password_receive:
            return jsonify({'ans': 'fail', 'msg': '비밀번호가 다릅니다'})


    doc = {
        'name':name_receive,
        'email':email_receive,
        'password':password_receive,
        'pwcf':pwcf_receive
    }
    db.diary.insert_one(doc)
    return jsonify({'ans':'success', 'msg': '회원가입 완료'})


# 로그인(POST) API
@app.route('/login/res', methods=['POST',"GET"])
def login():
    name_receive = request.form['name_give']
    password_receive = request.form['password_give']
    print(name_receive, password_receive)
    res = db.diary.find({}, {'_id': False})
    return jsonify({'ans': 'success', 'msg': '회원가입 완료'})
    # for list in res:
    #     # DB의 id와 비밀번호 확인
    #     if list['name'] == name_receive and list['password'] == password_receive:
    #         #세션 할당 후
    #         session['name'] = request.form['name_give']
    #         #
    #         return render_template(url_for(login_page))
    # return render_template(url_for(login_page))




# # 주문 목록보기(Read) API
# @app.route('/order', methods=['GET'])
# def view_orders():
#     orders = list(db.diary.find({},{'_id':False})) #조건
#     return jsonify({'all_orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)
    #



