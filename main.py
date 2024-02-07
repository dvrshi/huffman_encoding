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
        print(input_string)
        encoded_bytes, reverse_mapping = huffman_encode_string(input_string)
        print(encoded_bytes)
        write_file(encoded_bytes, reverse_mapping)
        # print("Encoded Bytes:", encoded_bytes)
        response_data = {'message': 'Data received successfully', 'processed_data': input_string}  
        return jsonify(response_data)
    elif request.method == 'GET':
        return "GET request received"
    else:
        return "Method not allowed"

@app.route('/decode_data', methods=['GET', 'POST'])
@cross_origin()
def decode_data():
    if request.method == 'POST':
        file_content = request.json['text_string']
        
        
        lines = file_content.strip().split('\n')
        encoded_bits = lines[0]
        
        reverse_mapping = {}
        if len(lines) > 1:
            reverse_mapping = {line.strip().split(':')[0]: line.strip().split(':')[1] for line in lines[1:]}

        
        binary_string = ''.join(filter(lambda x: x in '01', encoded_bits))
        bytes_data = bytes(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
        bytearray_data = bytearray(bytes_data)
        # print(bytearray_data)
        decode_data = huffman_decode_string(bytearray_data, reverse_mapping)
        response_data = {'processed_data': decode_data}  
        return jsonify(response_data)
    elif request.method == 'GET':
        return "GET request received"
    else:
        return "Method not allowed"


if __name__ == '__main__':
    app.run(debug=True)
