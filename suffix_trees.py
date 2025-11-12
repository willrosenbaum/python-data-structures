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

if __name__ == '__main__':
    text = 'prepossesses$'
    sorted_suffixes = sorted(suffixes(text))
    print(sorted_suffixes)
    lcp_array = lcp_array(text)
    print(lcp_array)