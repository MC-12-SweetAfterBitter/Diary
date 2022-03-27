from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('register.html')


# 회원가입(POST) API
@app.route('/register', methods=['POST'])
def user_infor():
    name_receive = request.form['name_give']
    email_receive = request.form['email_give']
    password_receive = request.form['password_give']
    pwcf_receive = request.form['pwcf_give']
    print(name_receive,email_receive,password_receive,pwcf_receive)

    res = db.diary.find({}, {'_id': False})


    for list in res:
        # 회원가입 시 중복 ID, Email 처리
        if list['name'] == name_receive or list['email'] == email_receive:
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


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.diary.find({},{'_id':False})) #조건
    return jsonify({'all_orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)
    #



