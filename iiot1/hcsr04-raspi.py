from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update_distance():
    data = request.get_json()
    if 'distance' in data:
        distance = data['distance']
        print(f"Received Distance: {distance} cm")
        return jsonify({'status': 'success', 'distance': distance}), 200
    else:
        return jsonify({'status': 'error', 'message': 'No distance data found'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Adjust the port as needed
