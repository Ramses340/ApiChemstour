from flask import Flask, jsonify, request
from entities.trip import Trip

app = Flask(__name__)

@app.route('/trips', methods=['GET'])
def trips():
    trips = Trip.get()
    return jsonify(trips)

@app.route('/trips', methods=['POST'])
def add_trip():
    data = request.get_json()
    name = data.get('name')
    city = data.get('city')
    country = data.get('country')
    latitude = data.get('latitude')
    longitude = data.get('longitude')


    result = Trip.add(name, city, country, latitude, longitude)
    if result:
        return jsonify(True)
    else:
        return jsonify({'error': 'Error al agregar el viaje'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
