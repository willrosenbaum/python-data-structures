def elias_encode(n: int) -> str:
    if n == 0:
        return '0'
    binary = format(n, 'b')
    return ''.join(['0' * (len(binary) - 1) + binary])

def elias_decode(encoded: str) -> int:
    if encoded == '0':
        return 0
    binary = encoded.lstrip('0')
    return int(binary, 2)

def rle_encode(text: str) -> str:
    encoded = f'{text[0]}'
    i = 0
    while i < len(text):
        run_length = 1
        while i < len(text) - 1 and text[i] == text[i+1]:
            run_length += 1
            i += 1
        encoded += elias_encode(run_length)
        print(f'run_length: {run_length}')
        i += 1
    return encoded

def rle_decode(encoded: str) -> str:
    decoded = ''
    cur_char = encoded[0]
    i = 1
    while i < len(encoded):
        # i is index of start of a run
        count = 0
        while encoded[i] == '0':
            i += 1
            count += 1
        binary = encoded[i:i+count+1]
        print(f'binary: {binary}')
        run_length = int(binary, 2)
        decoded += cur_char * run_length
        cur_char = '0' if cur_char == '1' else '1'
        i += count + 1
        
    return decoded

if __name__ == '__main__':
    example = '00000111110000000111000000000111'
    print(f'original string: {example}')
    encoded = rle_encode(example)
    print(f'encoded: {encoded}')
    decoded = rle_decode(encoded)
    print(f'decoded: {decoded}')
    assert decoded == example, 'Error: Decoded string does not match original string'