from flask import Flask, request, jsonify
from faker import Faker
from services.fakerService import FakerService
from services.fakerError import FakerError

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
LANG = 'ja_JP'


@app.route('/')
def hello():
    name = "こんにちは世界。"
    return name


@app.route('/person', methods=['GET'])
def person():
    lang = request.args.get('lang', LANG)
    seed = request.args.get('seed', None)
    count = request.args.get('count', None)

    service = FakerService(lang)

    return jsonify(service.execute('person'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
