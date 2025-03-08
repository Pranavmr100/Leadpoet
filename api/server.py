# api/server.py

import config
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit_leads', methods=['POST'])
def submit_leads():
    data = request.get_json()
    return jsonify({"message": f"Received leads: {data}"}), 200

@app.route('/leads', methods=['GET'])
def get_leads():
    return jsonify({"message": "Here are your leads (not really yet!)"}), 200

@app.route('/validation_status', methods=['GET'])
def validation_status():
    return jsonify({"message": "Validation status coming soon"}), 200

if __name__ == '__main__':
    app.run(host=config.API_HOST, port=config.API_PORT)