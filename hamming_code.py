import random
random.seed(4)

def encode_block(message: list[int]) -> list[int]:
    codeword = [0] * 8
    m_3 = message[3]
    m_2 = message[2]
    m_1 = message[1]
    m_0 = message[0]
    p_4 = m_3 ^ m_2 ^ m_1
    p_2 = m_3 ^ m_2 ^ m_0
    p_1 = m_3 ^ m_1 ^ m_0

    codeword[7] = m_3
    codeword[6] = m_2
    codeword[5] = m_1
    codeword[4] = p_4
    codeword[3] = m_0
    codeword[2] = p_2
    codeword[1] = p_1

    return codeword

def decode_block(message: list[int]) -> list[int]:
    x = message.copy()
    if len(x) == 7:
        x.insert(0, 0)
    p_4 = x[7] ^ x[6] ^ x[5] ^ x[4]
    p_2 = x[7] ^ x[6] ^ x[3] ^ x[2]
    p_1 = x[7] ^ x[5] ^ x[3] ^ x[1]
    index = 4 * p_4 + 2 * p_2 + p_1
    if index != 0:
        x[index] = 1 - x[index]
    decoded = [0] * 4
    decoded[3] = x[7]
    decoded[2] = x[6]
    decoded[1] = x[5]
    decoded[0] = x[3]
    return decoded

def to_string(message: list[int]) -> str:
    reversed = message.copy()
    reversed.reverse()
    if len(reversed) == 8:
        reversed.pop()
    return ''.join(str(x) for x in reversed)

def from_string(message: str) -> list[int]:
    array = [int(x) for x in message]
    array.reverse()
    return array

def is_codeword(message: list[int]) -> bool:
    x = message.copy()
    p_4 = x[7] ^ x[6] ^ x[5] ^ x[4]
    p_2 = x[7] ^ x[6] ^ x[3] ^ x[2]
    p_1 = x[7] ^ x[5] ^ x[3] ^ x[1]
    return 4 * p_4 + 2 * p_2 + p_1 == 0

def get_alphabet(message: str) -> dict[str, str]:
    letters = list(set(message))
    letters.sort()
    alphabet = {}
    for i in range(len(letters)):
        alphabet[letters[i]] = f'{i:04b}'
    return alphabet

def encode_with_alphabet(message: str, alphabet: dict[str, str]) -> str:
    encoded = []
    for letter in message:
        binary = alphabet[letter]
        codeword = encode_block(from_string(binary))
        encoded.append(to_string(codeword))
    return encoded

def decode_with_alphabet(message: list[str], alphabet: dict[str, str]) -> str:
    decoded = []
    for codeword in message:
        decoded_block = decode_block(from_string(codeword))
        decoded.append(to_string(decoded_block))
    return decoded

def flip_bit_random(word: str) -> str:
    flipped = [int(x) for x in word]
    index = random.randint(0, len(word) - 1)
    flipped[index] = 1 - flipped[index]
    return ''.join(str(x) for x in flipped)

def flip_bit(word: str, bit: int) -> str:
    flipped = [int(x) for x in word]
    flipped[bit] = 1 - flipped[bit]
    return ''.join(str(x) for x in flipped)

def get_random_message() -> str:
    return ''.join(str(random.randint(0, 1)) for _ in range(4))
    

if __name__ == '__main__':
    # letters = "ABCDEFGHIJKLMNOP"
    # alphabet = get_alphabet(letters)
    # message = "GOAL"
    # print([alphabet[x] for x in message])
    # encoded = encode_with_alphabet(message, alphabet)
    # print(encoded)
    # flipped = [flip_bit(x) for x in encoded]
    # print(flipped)
    # decoded = decode_with_alphabet(flipped, alphabet)
    # print(decoded)

    for i in range(1,11):
        print(f'Example {i}:')
        message = get_random_message()
        print(f'Message: {message}')

        codeword = to_string(encode_block(from_string(message)))
        print(f'Codeword: {codeword}')

        flip_bit_index = random.randint(0, 6)
        print(f'Flipping bit {7 - flip_bit_index}')
        flipped = flip_bit(codeword, flip_bit_index)
        print(f'Flipped: {flipped}')

        decoded = decode_block(from_string(flipped))
        print(f'Decoded: {to_string(decoded)}\n')


    # message = from_string("1001")
    # codeword = encode_block(message)
    # print(to_string(codeword))
    # decoded = decode_block(codeword)
    # print(to_string(decoded))

    


    # message = from_string("1011")
    # codeword = encode_block(message)
    # print(to_string(codeword))
    # decoded = decode_block(codeword)
    # print(to_string(decoded))