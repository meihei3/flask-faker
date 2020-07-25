from flask import Flask, request
from faker import Faker
from faker.config import AVAILABLE_LOCALES
from Services.FakerService import FakerService
from Services.FakerError import FakerError

app = Flask(__name__)
LANG = 'ja_JP'


@app.route('/')
def hello():
    name = "こんにちは世界。"
    return name


@app.route('/name', methods=['GET'])
def name():
    lang = request.args.get('lang', LANG)
    seed = request.args.get('seed', None)

    service = FakerService(lang, 0)
    if (service.error in (FakerError.NOT_SUPPORTED_LANG, FakerError.NOT_INTEGER_TYPE)):
        return {'message': 'error'}

    return service.faker.name()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
