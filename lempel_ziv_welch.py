def get_alphabet(text: str) -> list[str]:
    return sorted(list(set(text)))

def lzw_encode(text: str, alphabet: list[str]) -> tuple[list[int], dict]:
    dictionary = {}
    k = len(alphabet)
    for i in range(k):
        dictionary[alphabet[i]] = i
    encoded = []
    cur_phrase = text[0]
    for i in range(1,len(text)):
        cur_char = text[i]
        if cur_phrase + cur_char in dictionary:
            cur_phrase = cur_phrase + cur_char
        else:
            encoded.append(dictionary[cur_phrase])
            dictionary[cur_phrase+cur_char] = k
            k += 1
            cur_phrase = cur_char
    encoded.append(dictionary[cur_phrase])
    return encoded, dictionary

def lzw_decode(encoded: list[int], alphabet: list[str]) -> str:
    dictionary = {}
    lookup_table = []
    k = len(alphabet)
    for i in range(k):
        dictionary[alphabet[i]] = i
        lookup_table.append(alphabet[i])
    decoded_phrases = [lookup_table[encoded[0]]]
    next_phrase = decoded_phrases[0]
    for i in range(1, len(encoded)):
        cur_phrase = next_phrase
        next_codeword = encoded[i]
        if next_codeword == k:
            #print('hit special case!')
            next_phrase = cur_phrase + cur_phrase[0]
        else:
            next_phrase = lookup_table[next_codeword]
        decoded_phrases.append(next_phrase)
        dictionary[cur_phrase + next_phrase[0]] = k
        lookup_table.append(cur_phrase + next_phrase[0])
        k += 1
    return ''.join(decoded_phrases)

if __name__ == '__main__':
    print('Example 1:')
    text = 'ABABABACABABA'
    alphabet = get_alphabet(text)
    encoded, dictionary = lzw_encode(text, alphabet)
    print(f'text: {text}')
    print(f'alphabet: {alphabet}')
    print(f'encoded: {encoded}')
    binary = ''.join([format(ch, '04b') for ch in encoded])
    print(f'encoded in binary: {binary}')
    print(f'dictionary: {dictionary}')
    decoded = lzw_decode(encoded, alphabet)
    print(f'decoded: {decoded}\n')

    print('Example 2:')
    text = 'AAAAAGH!!!'
    alphabet = get_alphabet(text)
    encoded, dictionary = lzw_encode(text, alphabet)
    print(f'text: {text}')
    print(f'alphabet: {alphabet}')
    print(f'encoded: {encoded}')
    binary = ''.join([format(ch, '04b') for ch in encoded])
    print(f'encoded in binary: {binary}')
    print(f'dictionary: {dictionary}')
    decoded = lzw_decode(encoded, alphabet)
    print(f'decoded: {decoded}')
            