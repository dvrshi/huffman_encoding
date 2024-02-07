import heapq

class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if not isinstance(other, HuffmanCoding.HeapNode):
                return False
            return self.freq == other.freq

    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency):
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        if len(padded_encoded_text) % 8 != 0:
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            b.append(int(byte, 2))
        return b

    def compress_string(self, text):
        frequency = self.make_frequency_dict(text)
        self.make_heap(frequency)
        self.merge_nodes()
        self.make_codes()

        encoded_text = self.get_encoded_text(text)
        padded_encoded_text = self.pad_encoded_text(encoded_text)

        b = self.get_byte_array(padded_encoded_text)
        return b, self.reverse_mapping

    def decompress_string(self, encoded_bytes, reverse_mapping):
        bit_string = ""
        for byte in encoded_bytes:
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits

        padded_info = bit_string[:8]
        extra_padding = int(padded_info, 2)

        bit_string = bit_string[8:]
        encoded_text = bit_string[:-1 * extra_padding]

        current_code = ""
        decoded_text = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in reverse_mapping:
                character = reverse_mapping[current_code]
                decoded_text += character
                current_code = ""
        return decoded_text

def huffman_encode_string(input_string):
    huffman_coder = HuffmanCoding()
    encoded_bytes, reverse_mapping = huffman_coder.compress_string(input_string)
    return encoded_bytes, reverse_mapping

def huffman_decode_string(encoded_bytes, reverse_mapping):
    huffman_coder = HuffmanCoding()
    decoded_text = huffman_coder.decompress_string(encoded_bytes, reverse_mapping)
    return decoded_text

def write_file(encoded_bytes,reverse_mapping):
    encoded_bits = ''.join(format(byte, '08b') for byte in encoded_bytes)
    
    with open("trial.txt", 'w') as file:
        file.write(encoded_bits)
        file.write('\n')  
        for key, value in reverse_mapping.items():
            line = f"{key}:{value}\n"
            file.write(line) 

