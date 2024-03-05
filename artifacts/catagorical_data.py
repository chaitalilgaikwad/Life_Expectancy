from flask import Flask, jsonify, request
import os
import json
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Example: Assuming 'Status' is a categorical feature
status_encoder = LabelEncoder()
status_encoder.fit(['Developed', 'Developing'])

# Path to the artifacts folder
artifacts_folder = os.path.join(os.getcwd(), 'artifacts')

# Create the artifacts folder if it doesn't exist
if not os.path.exists(artifacts_folder):
    os.makedirs(artifacts_folder)

# Path to the JSON file for encoded categorical data
encoded_status_file = os.path.join(artifacts_folder, 'encoded_status.json')

# Encode and store categorical data in JSON file
encoded_status_data = {'Developed': int(status_encoder.transform(['Developed'])[0]),
                       'Developing': int(status_encoder.transform(['Developing'])[0])}

with open(encoded_status_file, 'w') as json_file:
    json.dump(encoded_status_data, json_file)

@app.route('/encode_status/<status>')
def encode_status(status):
    encoded_status = status_encoder.transform([status])[0]
    return jsonify({'encoded_status': encoded_status})

@app.route('/decode_status/<encoded_status>')
def decode_status(encoded_status):
    decoded_status = status_encoder.inverse_transform([int(encoded_status)])[0]
    return jsonify({'decoded_status': decoded_status})

if __name__ == '__main__':
    app.run(debug=True)
