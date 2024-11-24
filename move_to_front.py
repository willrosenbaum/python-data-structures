def move_to_front(text: str, alphabet: list[str]) -> list[int]:
    encoded = []
    for ch in list(text):
        encoded.append(alphabet.index(ch))
        alphabet.remove(ch)
        alphabet.insert(0,ch)
    return encoded

def get_alphabet(text: str) -> list[str]:
    return sorted(list(set(text)))

if __name__ == '__main__':
    text = 'anabanana'
    alphabet = get_alphabet(text)
    print(f'alphabet: {alphabet}')
    encoded = move_to_front(text, alphabet)
    print(f'text: {text}')
    print(f'encoded: {encoded}')