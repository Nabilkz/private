# first.py
from flask import Flask, request
app = Flask(__name__)

@app.route('/send_data', methods=['POST'])
def send_data():
    global input_1
    input_1 = request.form['input']
    return input_1

@app.route('/send_sent_data', methods=['GET'])
def send_sent_data():
    global input_1
    return input_1

@app.route('/get_data', methods=['POST'])
def get_data():
    global input1
    input1 = request.form['output']
    return input1

@app.route('/send_get_data', methods=['GET'])
def send_get_data():
    global input1
    return input1

while True:
    app.run()
