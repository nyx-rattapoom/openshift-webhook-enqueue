from flask import (
    Flask,
    request,
    jsonify
)
from pprint import pprint
from helper import (
    get_headers_dict,
    send_queue
)


application = Flask(__name__)


@application.route('/')
def home():
    response = {
        'status': 'ok'
    }
    return jsonify(response)


@application.route('/', methods=['POST'])
def handle():
    headers = request.headers
    headers = get_headers_dict(headers)
    body = request.get_json()
    accept_request = {
        'headers': headers,
        'body': body
    }
    send_queue(accept_request)
    response = {
        'status': 'ok'
    }
    return jsonify(response)


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
