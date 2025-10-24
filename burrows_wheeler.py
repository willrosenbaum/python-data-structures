from functools import cmp_to_key

def sentinel_compare_string(a: str, b: str, sentinel: str = '$') -> bool:
    if len(a) > len(b):
        a, b = b, a
    
    i = 0
    while i < len(a) and a[i] == b[i]:
        i += 1
    
    if i == len(a):
        if len(a) == len(b):
            return 0
        return -1
    
    if a[i] == sentinel:
        return -1
    
    if b[i] == sentinel:
        return 1
    
    return ord(a[i]) - ord(b[i])

def sentinel_compare_char(a: str, b: str, sentinel: str = '$'):
    if a == sentinel:
        return -1
    if b == sentinel: 
        return 1
    return ord(a) - ord(b)

def burrows_wheeler(text: str, sentinel: str = '$') -> str:
    if text[-1] != sentinel:
        text = text + sentinel
    shifts = []
    for i in range(len(text)):
        shifts.append(text[i:len(text)]+text[0:i])
    shifts = sorted(shifts, key=cmp_to_key(lambda s, t: sentinel_compare_string(s,t,sentinel)))

    return ''.join([s[-1] for s in shifts])

def inverse_burrows_wheeler(text: str, sentinel: str = '$') -> str:
    pairs = [(text[i], i) for i in range(len(text))]
    sorted_pairs = sorted(pairs, key=cmp_to_key(lambda a, b: sentinel_compare_char(a[0], b[0], sentinel)))
    next_index = sorted_pairs[0][1]
    bw_inverse = ''
    while next_index != 0:
        bw_inverse = bw_inverse + sorted_pairs[next_index][0]
        next_index = sorted_pairs[next_index][1]
    return bw_inverse
    

if __name__ == '__main__':
    text = 'evennesses'
    bw = burrows_wheeler(text)
    print(f"original text: {text}")
    print(f"burrow-wheeler transformed: {bw}")
    print(f"burrows-wheeler inverse: {inverse_burrows_wheeler(bw)}")