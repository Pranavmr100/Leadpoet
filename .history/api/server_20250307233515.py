# api/server.py

from flask import Flask, request, jsonify
from .. import config
app = Flask(__name__)

# api/server.py

from flask import Flask, request, jsonify
from .. import config

app = Flask(__name__)

@app.route('/submit_leads', methods=['POST'])
def submit_leads():
    # Get the data sent to us
    data = request.get_json()
    return jsonify({"message": f"Received leads: {data}"}), 200

@app.route('/leads', methods=['GET'])
def get_leads():
    # Placeholder for buyer access
    return jsonify({"message": "Here are your leads (not really yet!)"}), 200

@app.route('/validation_status', methods=['GET'])
def validation_status():
    # Placeholder for checking status
    return jsonify({"message": "Validation status coming soon"}), 200

if __name__ == '__main__':
    app.run(host=config.API_HOST, port=config.API_PORT)