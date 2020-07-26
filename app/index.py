from flask import Flask, request, jsonify, abort
from faker import Faker
from services.fakerService import FakerService
from services.fakerError import FakerError

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/person', methods=['GET'])
def person():
    seed = request.args.get('seed', None, type=int)
    count = request.args.get('count', None, type=int)

    service = FakerService(seed, count)

    return jsonify(service.execute('person'))


@app.route('/person/<string:sex>', methods=['GET'])
def person_sexes(sex: str):
    seed = request.args.get('seed', None, type=int)
    count = request.args.get('count', None, type=int)

    service = FakerService(seed, count)

    if sex == FakerService.FEMALE:
        return jsonify(service.execute(f'person_{FakerService.FEMALE}'))
    elif sex == FakerService.MALE:
        return jsonify(service.execute(f'person_{FakerService.MALE}'))

    return abort(404)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
