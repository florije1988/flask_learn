# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask, request, jsonify
import urllib

app = Flask(__name__)


def do_something(name, age, **kwargs):
    return 10


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    args, data, form = request.args, request.data, request.form
    a = urllib.urlencode({'name': 'fubo qing', 'address': 'beijing'})
    print a
    params = {"name": "fuboqing", "age": 10, "desc": "haoren"}
    res = do_something(**params)
    return jsonify({"access_token": "ACCESS_TOKEN", "expires_in": 7200})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
