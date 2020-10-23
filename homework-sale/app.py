from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML 화면 보기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_recv = request.form['name_give']
    count_recv = request.form['count_give']
    address_recv = request.form['address_give']
    phone_recv = request.form['phone_give']

    doc = {
        'name' : name_recv,
        'count' : count_recv,
        'address' : address_recv,
        'phone' : phone_recv
    }

    db.homework.insert_one(doc)

    return jsonify({'result': 'success'})

#name, count, address, phone

# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.homework.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)