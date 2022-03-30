from flask import Flask, render_template, jsonify, request, session, redirect, url_for, escape
from datetime import timedelta
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import time, flask_abort
app = Flask(__name__)



client = MongoClient('localhost', 27017)
db = client.SweetAfterBitter

app = Flask(__name__)
app.secret_key = 'secretkey_soieoefs0f39fnsjdbf'  # secret_key는 서버상에 동작하는 어플리케이션 구분하기 위해 사용하고 복잡하게 만들어야 합니다.
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(seconds=5) # 로그인 지속시간을 정합니다. 현재 1분
app.config["MONGO_URI"] = "mongodb://localhost:27017/SweetAfterBitter"
app.config['SECRET_KEY'] = 'psswrd'

mongo = PyMongo(app)
aaa = mongo.db.diary

# 홈 화면 보여주기
@app.route('/')
def main_page():
    if "email" in session:
        return render_template('main.html',
                               Email = session['email']
                               )
    else :
        return render_template('main.html')

# 회원가입 화면 보여주기
@app.route('/signup')
def signup_page():
    return render_template('signup.html')

# 로그인 화면 보여주기
@app.route('/login')
def login_page():
    if "email" in session:
        # return jsonify({"ans":"success"},{"msg" : "환영합니다 {}님".format(escape(session['name']))})
        # return "환영합니다 {}님".format(escape(session['email']))
        return redirect(url_for('main_page'))
    else :
        return render_template('login.html')

# 개인 일기장 보여주기
@app.route('/personal')
def personal_main_page():
    return render_template('personal_main.html')


# 회원가입(POST) API
@app.route('/signup/info', methods=['POST'])
def signup():
    name_receive = request.form['name_give']
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']
    pwcf_receive = request.form['pwcf_give']
    print(name_receive,email_receive,password_receive,pwcf_receive)

    res = db.users.find({}, {'_id': False})


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
    db.users.insert_one(doc)
    return jsonify({'ans':'success', 'msg': '회원가입 완료'})

# 로그인(POST) API
@app.route('/login/info', methods=['POST', "GET"])
def login():
    if request.method == 'POST':
        email_receive = request.form['em']
        password_receive = request.form['pw']
        print(email_receive, password_receive)
        res = db.users.find({}, {'_id': False})

        for i in res:
            print(i)
            if i['email'] == email_receive and i['password'] == password_receive:
                session.clear()
                # 세션 할당 후
                session['email'] = email_receive
                print("세션 Id : " + session['email'])
                return redirect(url_for('login_page'))
            pass


        return render_template("login.html")

# 글쓰기(POST) API
@app.route('/personal', methods=['GET', 'POST'])
def write():
    if request.method == "POST":
        cur_time = time.strftime("%y%m%d_%H%M%S")
        title = request.form.get('title')
        contents = request.form.get('contents')
        year = request.form.get('year')
        month = request.form.get('month')
        day = request.form.get('day')
        date = year + "년 " + month + "월 " + day +"일"
        db = {
            'title': title,
            'contents': contents,
            'pubdate': cur_time,
            'date' : date
        }
        db = aaa.insert_one(db)

        return redirect(url_for('diary_rd', idx=db.inserted_id))
    else:
        return render_template('personal_main.html')




# 글보기(GET) API
@app.route("/bulletin_rd")
def bulletin_rd():
    print("arg :", request.args.get("idx"))
    if request.args.get("idx"):
        idx = request.args.get("idx")
        aaa = mongo.db.diary
        print("idx :", type(idx))
        print("ObjectId(idx) :", type(ObjectId(idx)))
        print(aaa.find_one({"_id": ObjectId(idx)}))
        if aaa.find_one({"_id": ObjectId(idx)}):
            diary_data = aaa.find_one({"_id": ObjectId(idx)})
            # db에서 찾을때 _id 값은 string이 아닌 ObjectId로 바꿔야함
            print(diary_data)
            if diary_data != "":
                db_data = {
                    "id": diary_data.get("_id"),
                    "title": diary_data.get("title"),
                    "contents": diary_data.get("contents"),
                    "pubdate": diary_data.get("pubdate")
                }

                return render_template("diary_rd.html", db_data=db_data)
        return abort(404)
    return abort(404)


# 로그아웃(POST) API
@app.route('/logout')
def logout():
    session.pop('email', None)
    return jsonify({'msg': '로그아웃 하였습니다.'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)

