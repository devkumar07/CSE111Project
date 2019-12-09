from database.dbscript import *
import json

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/init', methods=['GET'])
def init():
    print("Test")
    o = get_main_table()
    print("The type is ", type(o))
    output = json.dumps(get_main_table())
    return output

if __name__ == '__main__':
    app.run(debug=False, threaded=True, host= '0.0.0.0')