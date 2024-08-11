from flask import Flask, render_template, request
from os.path import dirname, abspath, join
from json import loads, dumps
import random
from core import search
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/s', methods=['GET'])
def about():
    try:
        content = []
        request_data, s = request.args.get('q'), request.args.get('s')
        result = search.search(request_data, s)
        for obj in result:
            try:
                content.append([obj.title, obj.summary, obj.url])
            except Exception as e:
                print(e)
                print(obj.title, obj.summary, obj.url)
        print(content)
    except Exception as e:
        return "Something's wrong. " + str(e), 500, {"Content-Type": "application/json"}
        # print(e)
        # return content, 200, {"Content-Type": "application/json"}
    return content, 200, {"Content-Type": "application/json"}


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='127.0.0.1', port=2333)
