from flask import Flask, request, jsonify
from faker import Faker
from services.fakerService import FakerService
from services.fakerError import FakerError

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello():
    name = "こんにちは世界。"
    return name


@app.route('/person', methods=['GET'])
def person():
    seed = request.args.get('seed', None, type=int)
    count = request.args.get('count', None, type=int)

    service = FakerService(seed, count)

    return jsonify(service.execute('person'))


@app.route('/person/female', methods=['GET'])
def person_female():
    seed = request.args.get('seed', None, type=int)
    count = request.args.get('count', None, type=int)

    service = FakerService(seed, count)

    return jsonify(service.execute('person_female'))


@app.route('/person/male', methods=['GET'])
def person_male():
    seed = request.args.get('seed', None, type=int)
    count = request.args.get('count', None, type=int)

    service = FakerService(seed, count)

    return jsonify(service.execute('person_male'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
