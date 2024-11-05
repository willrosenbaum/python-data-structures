from curses.ascii import STX, ETX

## Code taken from Wikipedia:
## https://en.wikipedia.org/wiki/Burrows–Wheeler_transform

def bwt(s: str, start=chr(STX), end=chr(ETX)) -> str:
    """
    Apply Burrows–Wheeler transform to input string.

    >>> bwt('BANANA')
    '\x03ANNB\x02AA'
    >>> bwt('BANANA', start='^', end='$')
    '^ANNB$AA'
    >>> bwt('BANANA', start='%', end='$')
    '%A$NNB%AA'
    """
    assert (
        start not in s and end not in s
    ), "Input string cannot contain start and end characters"
    s = f"{start}{s}{end}"  # Add start and end of text marker

    # Table of rotations of string
    table = sorted(f"{s[i:]}{s[:i]}" for i, c in enumerate(s))
    last_column = [row[-1:] for row in table]  # Last characters of each row
    return "".join(last_column)  # Convert list of characters into string

def inverse_bwt(r: str, start=chr(STX), end=chr(ETX)) -> str:
    """
    Apply inverse Burrows–Wheeler transform.

    >>> inverse_bwt('\x03ANNB\x02AA')
    'BANANA'
    >>> inverse_bwt('^ANNB$AA', start='^', end='$')
    'BANANA'
    >>> inverse_bwt('%A$NNB%AA', start='%', end='$')
    'BANANA'
    """
    str_len = len(r)
    table = [""] * str_len  # Make empty table
    for _ in range(str_len):
        table = sorted(rc + tc for rc, tc in zip(r, table))  # Add a column of r

    # Iterate over and check whether last character ends with end character or not
    s = next((row for row in table if row.endswith(end)), "")

    # Retrieve data from array and get rid of start and end markers
    return s.rstrip(end).lstrip(start)

if __name__ == "__main__":
    print('bwt("intestine") = ', bwt("intestine"))
    print('inverse_bwt(bwt("intestine")) = ', inverse_bwt(bwt("intestine")))
