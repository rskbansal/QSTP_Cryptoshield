def decode_from_binary(binary_str):
    decoded_string = ''
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        decoded_string += chr(int(byte, 2))
    return decoded_string

def decode_multiple_times(binary_str, times):
    for i in range(times):
        binary_str = decode_from_binary(binary_str)
    return binary_str

if __name__ == "__main__":
    with open('in.txt', 'r') as f:
        input_binary = f.read()

    num_decodings = 6
    decoded_string = decode_multiple_times(input_binary, num_decodings)
    print(decoded_string)