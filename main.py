# backend.py
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from huffman import *
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/process_data', methods=['GET', 'POST'])
@cross_origin()
def process_data():
    # print(data.Type)
    if request.method == 'POST':
        data = request.json 
        input_string = data['text_string']
        encoded_bytes, reverse_mapping = huffman_encode_string(input_string)
        write_file(encoded_bytes, reverse_mapping)
        print("Encoded Bytes:", encoded_bytes)
        response_data = {'message': 'Data received successfully', 'processed_data': input_string}  
        return jsonify(response_data)
    elif request.method == 'GET':
        return "GET request received"
    else:
        return "Method not allowed"

@app.route('/decode_data', methods=['GET', 'POST'])
@cross_origin()


if __name__ == '__main__':
    app.run(debug=True)
