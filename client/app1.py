import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# enable CORS,解决跨域问题
CORS(app, resources={r'/*': {'origins': '*'}})


# app.jinja_env.variable_start_string = '%%'
# app.jinja_env.variable_end_string = '%%'

@app.route('/json/')
def json():
    data = request.args.to_dict()
    # dat = data["data"]
    print(data)
    rst = {
    "name":"网站",
    "num":3,
    "sites": [
        { "name":"Google", "info":[ "Android", "Google 搜索", "Google 翻译" ] },
        { "name":"Runoob", "info":[ "菜鸟教程", "菜鸟工具", "菜鸟微信" ] },
        { "name":"Taobao", "info":[ "淘宝", "网购" ] }
    ]
}
    return rst

@app.route('/ajax/')
def ajax():
    rst = {
        "list": [
            { "id": 1,"price": { "name": '项目一', "resData": [
                {"name": '订购费用', "value": 12},
                {"name": '饲养费用', "value": 18},
                {"name": '实验费用', "value": 8},
                {"name": '其他费用', "value": 10},
            ]}
            #   }, { "id": 2,"price": { "name": '项目二',"resData": [
            #     {"name": '订购费用', "value": 18},
            #     {"name": '饲养费用', "value": 10},
            #     {"name": '实验费用', "value": 20},
            #     {"name": '其他费用', "value": 9},
            # ]}
        }]
    }

    return rst

@app.route('/vue/<aa>')
def vue(aa):
    if aa == "aa":
        rst = {
            "list": [
                {"categories": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                 "data": [3, 2, 4, 4, 5]},
                {"categories": ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"],
                 "data": [23, 22, 24, 24, 25]}
            ]}
    else:
        rst = {
            "list": [
                {"categories": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                 "data": [103, 102, 104, 104, 105]},
                {"categories": ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"],
                 "data": [123, 122, 124, 124, 125]}
            ]}

    return rst


@app.route('/vue1/')
def vue1():
    rst = {
        "categories": [ "1","2","3","4", "5", "6","7", "8","9","10", "11", "12" ],
        "data": [3, 2, 4,  4, 5 ]
    }

    return rst

@app.route('/route_ajax/<item>')
def route_ajax(item):
    rst = {
        "categories": [ "1","2","3","4", "5", "6","7", "8","9","10", "11", "12" ],
        "data": [3, 2, 4,  4, 5 ]
    }

    return rst

@app.route('/table/<page>/<search>')
def table(page,search):
    if search == 'aa':
        aaa = [
                  { 'id': 10001, 'name': 'sst1', 'nickname': 'T1', 'role': 'Develop', 'sex': '1', 'age': 28, 'address': 'Shenzhen' },
                  { 'id': 10002, 'name': 'sst2', 'nickname': 'T2', 'role': 'Test', 'sex': '0', 'age': 22, 'address': 'Guangzhou' },
                  { 'id': 10003, 'name': 'sst3', 'nickname': 'T3', 'role': 'PM', 'sex': '1', 'age': 32, 'address': 'Shanghai' },
                  { 'id': 10004, 'name': 'sst4', 'nickname': 'T4', 'role': 'Designer', 'sex': '0', 'age': 23, 'address': 'Shenzhen' },
                  { 'id': 10005, 'name': 'sst5', 'nickname': 'T5', 'role': 'Develop', 'sex': '0', 'age': 30, 'address': 'Shanghai' },
                  { 'id': 10006, 'name': 'sst6', 'nickname': 'T6', 'role': 'Develop', 'sex': '0', 'age': 27, 'address': 'Shanghai' },
                  { 'id': 10007, 'name': 'sst7', 'nickname': 'T1', 'role': 'Develop', 'sex': '1', 'age': 28, 'address': 'Shenzhen' },
                  { 'id': 10008, 'name': 'ss8', 'nickname': 'T2', 'role': 'Test', 'sex': '0', 'age': 22, 'address': 'Guangzhou' },
                  { 'id': 10009, 'name': 'sst9', 'nickname': 'T3', 'role': 'PM', 'sex': '1', 'age': 32, 'address': 'Shanghai' },
                  { 'id': 100010, 'name': 'sst10', 'nickname': 'T4', 'role': 'Designer', 'sex': '0', 'age': 23, 'address': 'Shenzhen' },
                  { 'id': 100011, 'name': 'sst11', 'nickname': 'T5', 'role': 'PM', 'sex': '0', 'age': 35, 'address': 'Shenzhen' },
                  { 'id': 100012, 'name': 'sst12', 'nickname': 'T6', 'role': 'Designer', 'sex': '1', 'age': 25, 'address': 'Shanghai' },
                  { 'id': 100013, 'name': 'sst13', 'nickname': 'T9', 'role': 'Develop', 'sex': '1', 'age': 33, 'address': 'Shenzhen' },
                  { 'id': 100014, 'name': 'sst14', 'nickname': 'T6', 'role': 'Develop', 'sex': '0', 'age': 21, 'address': 'Shanghai' },
                  { 'id': 100015, 'name': 'sst15', 'nickname': 'T6', 'role': 'Develop', 'sex': '0', 'age': 19, 'address': 'Shanghai' },
                  { 'id': 100016, 'name': 'sst16', 'nickname': 'T8', 'role': 'Develop', 'sex': '1', 'age': 29, 'address': 'Shenzhen' }
        ]
    else:
        aaa = [
            {'id': 10001, 'name': 'Test1', 'nickname': '<a href="https://igv.org/web/release/2.10.4/examples/interact.html">我是链接a1</a>', 'role': 'Develop', 'sex': '1', 'age': 28,'address': 'Shenzhen'},
            {'id': 10002, 'name': 'Test2', 'nickname': '<a href="http://localhost:8080/#/url?id=a2">我是链接a2</a>', 'role': 'Test', 'sex': '0', 'age': 22,'address': 'Guangzhou'},
            {'id': 10003, 'name': 'Test3', 'nickname': '<a href="http://localhost:8080/#/url?id=https://igv.org/web/release/2.10.4/examples/interact.html">我是链接a3</a>', 'role': 'PM', 'sex': '1', 'age': 32, 'address': 'Shanghai'},
            {'id': 10004, 'name': 'Test4', 'nickname': '<a href="http://localhost:8080/#/url?id=a4">我是链接a4</a>', 'role': 'Designer', 'sex': '0', 'age': 23, 'address': 'Shenzhen'},
            {'id': 10005, 'name': 'Test5', 'nickname': '<a href="http://localhost:8080/#/url?id=a5">我是链接a5</a>', 'role': 'Develop', 'sex': '0', 'age': 30,  'address': 'Shanghai'},
            {'id': 10006, 'name': 'Test6', 'nickname': '<a href="http://localhost:8080/#/url?id=a6">我是链接a6</a>', 'role': 'Develop', 'sex': '0', 'age': 27, 'address': 'Shanghai'},
            {'id': 10007, 'name': 'Test7', 'nickname': '<a href="http://localhost:8080/#/url?id=a7">我是链接a7</a>', 'role': 'Develop', 'sex': '1', 'age': 28, 'address': 'Shenzhen'},
            {'id': 10008, 'name': 'Test8', 'nickname': '<a href="http://localhost:8080/#/url?id=a8">我是链接a8</a>', 'role': 'Test', 'sex': '0', 'age': 22, 'address': 'Guangzhou'},
            {'id': 10009, 'name': 'Test9', 'nickname': '<a href="http://localhost:8080/#/url?id=a9">我是链接a9</a>', 'role': 'PM', 'sex': '1', 'age': 32, 'address': 'Shanghai'},
            {'id': 100010, 'name': 'Test10', 'nickname': '<a href="http://localhost:8080/#/url?id=a10">我是链接a10</a>', 'role': 'Designer', 'sex': '0', 'age': 23, 'address': 'Shenzhen'},
            {'id': 100011, 'name': 'Test11', 'nickname': '<a href="http://localhost:8080/#/url?id=a11">我是链接a11</a>', 'role': 'PM', 'sex': '0', 'age': 35, 'address': 'Shenzhen'},
            {'id': 100012, 'name': 'Test12', 'nickname': '<a href="http://localhost:8080/#/url?id=a12">我是链接a12</a>', 'role': 'Designer', 'sex': '1', 'age': 25, 'address': 'Shanghai'},
            {'id': 100013, 'name': 'Test13', 'nickname': '<a href="http://localhost:8080/#/url?id=a13">我是链接a13</a>', 'role': 'Develop', 'sex': '1', 'age': 33, 'address': 'Shenzhen'},
            {'id': 100014, 'name': 'Test14', 'nickname': '<a href="http://localhost:8080/#/url?id=a14">我是链接a14</a>', 'role': 'Develop', 'sex': '0', 'age': 21, 'address': 'Shanghai'},
            {'id': 100015, 'name': 'Test15', 'nickname': '<a href="http://localhost:8080/#/url?id=a15">我是链接a15</a>', 'role': 'Develop', 'sex': '0', 'age': 19, 'address': 'Shanghai'},
            {'id': 100016, 'name': 'Test16', 'nickname': '<a href="http://localhost:8080/#/url?id=a16">我是链接a16</a>', 'role': 'Develop', 'sex': '1', 'age': 29, 'address': 'Shenzhen'}
        ]

    length = len(aaa)
    start = 3*(int(page)-1)
    end = 3*int(page)
    rst = {
        "lens":length,
        "categories": aaa[start:end]
    }
    print(aaa)
    return rst



if __name__ == '__main__':
    app.run()
