from flask import Flask, render_template, jsonify, request, session, redirect, url_for, escape
from datetime import timedelta
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import time, flask_abort

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)

app = Flask(__name__)
app.secret_key = 'secretkey_soieoefs0f39fnsjdbf'  # secret_key는 서버상에 동작하는 어플리케이션 구분하기 위해 사용하고 복잡하게 만들어야 합니다.
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(seconds=1800) # 로그인 지속시간을 정합니다. 현재 1분
app.config["MONGO_URI"] = "mongodb://localhost:27017/SweetAfterBitter"
app.config['SECRET_KEY'] = 'psswrd'

mongo = PyMongo(app)

db = client.SweetAfterBitter
aaa = mongo.db.diary
bbb = mongo.db.diary2


# 메인 홈페이지 (HTML 화면 보여주기)
@app.route('/')
def main():
    if "email" in session:
        # return jsonify({"ans":"success"},{"msg" : "환영합니다 {}님".format(escape(session['name']))})
        # return "환영합니다 {}님".format(escape(session['email']))
        return render_template('main.html', Email=session['email'], Name=session['name'])
    else:
        return render_template('main.html')


# 공감 다이어리 페이지
@app.route('/gonggam')
def gonggam():
    if "email" in session:
        # return jsonify({"ans":"success"},{"msg" : "환영합니다 {}님".format(escape(session['name']))})
        # return "환영합니다 {}님".format(escape(session['email']))
        return render_template('gonggam_main.html', Email=session['email'], Name=session['name'])
    else:
        return render_template('gonggam_main.html')


# 개인 다이어리 페이지
@app.route('/personal')
def personal():
    if "email" in session:
        # return jsonify({"ans":"success"},{"msg" : "환영합니다 {}님".format(escape(session['name']))})
        # return "환영합니다 {}님".format(escape(session['email']))
        return render_template('personal_main.html', Email=session['email'], Name=session['name'])
    else :
        return render_template('login.html')


# 로그인 페이지
@app.route('/login')
def login_page():
    if "email" in session:
        # return jsonify({"ans":"success"},{"msg" : "환영합니다 {}님".format(escape(session['name']))})
        # return "환영합니다 {}님".format(escape(session['email']))
        return render_template('main.html', Email=session['email'], Name=session['name'])
    else :
        return render_template('login.html')


# 회원가입 페이지
@app.route('/signup')
def signup():
    return render_template('signup.html')


####################################################


# 회원가입(POST) API
@app.route('/signup', methods=['POST'])
def user_infor():
    name_receive = request.form['name_give']
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']
    pwcf_receive = request.form['pwcf_give']

    res = db.users.find({}, {'_id': False})

    for list in res:
        # 공백 처리, 해당 부분에서 약간의 오류를 발생시키면 html 스크립트 공백체크가 작동한다..
        if name_receive == '' or email_receive == '' or password_receive == '' or pwcf_receive == '':
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

    return jsonify({'ans':'success', 'msg': '가입완료'})


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
                name = db.users.find_one({'email':session['email']})
                session['name'] = name['name']
                print("세션 Id : " + session['email'])
                print(name['name'])
                return redirect(url_for('login_page'))
            pass


        return render_template("login.html")


# 개인 글쓰기(POST) API
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
        if 'email' in session:
            id = session['email']

        db = {
            'email' : id,
            'title': title,
            'contents': contents,
            'pubdate': cur_time,
            'date' : date
        }
        aaa.insert_one(db)

        redirect(url_for('bulletin_rd'))
        return jsonify({'ans': 'success', 'msg': "작성 완료"})
    else:
        return render_template('personal_main.html')



# 개인 글보기(GET) API
@app.route("/bulletin_rd", methods=['GET'])
def bulletin_rd():
    # diary_data = list(aaa.find({},{'_id':False}))
    diary_data = list(aaa.find({'email':session['email']}, {'_id': False}).sort('date', 1))
    # test = list(aaa.find({}))
    print(diary_data)
    # print(diary_data)
    # diary_data = list(db.diary.find({},{'_id':False}).sort({'date:1'}))
    # diary_data = list(aaa.find().sort({'date': 1}))
    
    return jsonify({'all_data': diary_data})

# 공유 글쓰기(POST) API
@app.route('/public', methods=['GET', 'POST'])
def write2():
    if request.method == "POST":
        cur_time = time.strftime("%y%m%d_%H%M%S")
        name = request.form.get('name')
        title = request.form.get('title')
        contents = request.form.get('contents')

        db = {
            'name' : name,
            'title': title,
            'contents': contents,
            'pubdate': cur_time,
            'like' : 0
        }
        bbb.insert_one(db)

        redirect(url_for('bulletin_rd2'))
        return jsonify({'ans': 'success', 'msg': "작성 완료"})
    else:
        return render_template('gonggam_main.html')



# 공유 글보기(GET) API
@app.route("/bulletin_rd2", methods=['GET'])
def bulletin_rd2():
    # diary_data = list(aaa.find({},{'_id':False}))
    diary_data = list(bbb.find({}, {'_id': False}).sort('pubdate', 1))
    # test = list(aaa.find({}))
    # print(diary_data)
    # print(diary_data)
    # diary_data = list(db.diary.find({},{'_id':False}).sort({'date:1'}))
    # diary_data = list(aaa.find().sort({'date': 1}))
    return jsonify({'all_data': diary_data})

@app.route('/api/like', methods=['POST'])
def like_star():
    # 이름 받음
    name_receive = request.form['name']
    #이름으로 찾음
    #추가로 find_one은 하나의 자료만 찾으면 되니 list를 사용하지 않는다.
    target_star = db.diary2.find_one({'name':name_receive})
    #like 값 가져옴
    cur_like = target_star['like']
    #새로운 like 값 갱신을 위해 임시 저장 변수
    new_like = cur_like + 1
    print(name_receive)
    print(target_star)
    print(new_like)
    #갱신 , (조건, set+바꿀값)
    db.diary2.update_one({'name': name_receive}, {'$set': {'like': new_like}})
    return jsonify({'msg': 'like +1'})





# 로그아웃(POST) API
@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('name', None)
    return render_template('main.html')

##########################################################

if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)