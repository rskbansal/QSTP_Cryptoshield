def encode_to_binary(s):
    binary_string = ''.join(format(ord(char), '08b') for char in s)
    return binary_string

def encode_multiple_times(s, times):
    for _ in range(times):
        s = encode_to_binary(s)
    return s

if __name__ == "__main__":
    input_string = 'QSTP{FUcCk_b1nary!?}'
    encoded_string = encode_multiple_times(input_string, 6)
    
    with open('out.txt','w') as f:
        f.write(encoded_string)
