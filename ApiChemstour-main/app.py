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

@app.route('/trips/<int:tripId>', methods=['DELETE'])
def delete_trip(tripId):
    result = Trip.delete(tripId)
    if isinstance(result, int) and result > 0:
        return jsonify(True)
    else:
        return jsonify({'error': f'Error al eliminar el viaje con ID {tripId}'}), 500


@app.route('/trips/<int:tripId>', methods=['PUT'])
def update_trip(tripId):
    data = request.get_json()
    name = data.get('name')
    city = data.get('city')
    country = data.get('country')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    trip = Trip(name, city, country, latitude, longitude)
    result = Trip.update(tripId, trip)
    if isinstance(result, int) and result > 0:
        return jsonify(True)
    else:
        return jsonify({'error': f'Error al actualizar el viaje con ID {tripId}'}), 500
