def move_to_front(text: str, alphabet: list[str]) -> list[int]:
    encoded = []
    for ch in list(text):
        encoded.append(alphabet.index(ch))
        alphabet.remove(ch)
        alphabet.insert(0,ch)
    return encoded

def get_alphabet(text: str) -> list[str]:
    return sorted(list(set(text)))

def inverse_move_to_front(encoded: list[int], alphabet: list[str]) -> str:
    decoded = []
    for index in encoded:
        decoded.append(alphabet[index])
        alphabet = [alphabet[index]]+alphabet[0:index]+alphabet[index+1:len(alphabet)]
    return ''.join(decoded)


def print_example(text: str) -> None:
    alphabet = get_alphabet(text)
    print(f'alphabet: {alphabet}')
    encoded = move_to_front(text, alphabet.copy())
    print(f'text: {text}')
    print(f'encoded: {encoded}')
    decoded = inverse_move_to_front(encoded, alphabet.copy())
    print(f'decoded: {decoded}')

if __name__ == '__main__':
    print('Example 1:')
    print_example('lallapalooza')
    print('Example 2:')
    print_example('bananas')
    print('Example 3:')
    print_example('ratatat')
    print('Example 4:')
    print_example('piripiri')
    print('Example 5:')
    print_example('minimism')