def suffixes(text: str) -> list[str]:
    return [text[i:] for i in range(len(text))]

def lcp_array(text: str) -> list[int]:
    lcp_array = [0] * len(text)
    sorted_suffixes = sorted(suffixes(text))

    for i in range(len(sorted_suffixes)-1):
        for j in range(min(len(sorted_suffixes[i]),len(sorted_suffixes[i+1]))):
            if sorted_suffixes[i][j] == sorted_suffixes[i+1][j]:
                lcp_array[i] += 1
            else:
                break
    return lcp_array

def suffix_array(text: str) -> list[int]:
    return sorted(range(len(text)), key=lambda i: text[i:])

def rank_array_from_suffix_array(sa: list[int]) -> list[int]:
    rank_array = [0] * len(sa)
    for i in range(len(sa)):
        rank_array[sa[i]] = i
    return rank_array

def distinct_letters(text: str) -> list[str]:
    return sorted(list(set(text)))

def print_example(text: str) -> None:
    print(f'text: {text}')
    print(f'distinct_letters: {distinct_letters(text)}')
    sorted_suffixes = sorted(suffixes(text))
    print(sorted_suffixes)
    lcp = lcp_array(text)
    print('lcp: ', lcp)
    print('suffix_array: ', suffix_array(text))
    print('rank_array: ', rank_array_from_suffix_array(suffix_array(text)))

if __name__ == '__main__':
    text = 'prepossesses$'
    print_example(text)
    text = 'bananas$'
    print_example(text)
    text = 'ratatat$'
    print_example(text)
    text = 'piripiri$'
    print_example(text)
    text = 'cabacababaca$'
    print_example(text)