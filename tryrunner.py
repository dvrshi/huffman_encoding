from trial import huffman_encode_string, huffman_decode_string


input_string = "devarshi sanghani"
encoded_bytes, reverse_mapping = huffman_encode_string(input_string)

print("Original String:", input_string)
print("Encoded Bytes:", encoded_bytes)


encoded_bits = ''.join(format(byte, '08b') for byte in encoded_bytes)
with open("binary.txt", 'w') as file:
    file.write(encoded_bits)
    file.write('\n')  # Encode newline character as bytes
    for key, value in reverse_mapping.items():
        line = f"{key}:{value}\n"
        file.write(line) 


reverse_mapping = {}
encoded_bytes=None
with open('binary.txt', 'r') as file:
        encoded_bits = file.readline().strip()  # Read the first line (encoded bits)
        for line in file:
            line = line.strip()
            if not line:
                # Skip empty lines
                continue
            key, value = line.split(":")
            # print(key, value)
            reverse_mapping[key] = value

encoded_bytes = bytes(int(encoded_bits[i:i+8], 2) for i in range(0, len(encoded_bits), 8))
encoded_bytes_str = encoded_bytes.hex()  # Convert bytes to hexadecimal string
encoded_bytes_as_bytearray = bytearray.fromhex(encoded_bytes_str)  # Convert hexadecimal string back to bytearray

# print("Encoded Read Bytes as bytearray:", encoded_bytes_as_bytearray)
decoded_text = huffman_decode_string(encoded_bytes_as_bytearray, reverse_mapping)
print("Decoded Text:", decoded_text)
