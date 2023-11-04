from flask import Flask, request, jsonify, make_response
from os import environ

app = Flask(__name__)

# Set initial value
value = 0


@app.route('/test', methods=['GET'])
def test():
    global value
    value = 0
    return jsonify({'value': "The long string is: " + str(value)})


if __name__ == '__main__':
    app.run()
