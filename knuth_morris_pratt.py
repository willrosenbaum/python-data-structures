import random

# random.seed(42) # random seed for Fall 2024 Examples
random.seed(10)


def get_alphabet(pattern: str) -> list[str]:
    return sorted(list(set(pattern)))

def generate_dfa_table(pattern: str) -> list[dict[str, int]]:
    alphabet = get_alphabet(pattern)
    dfa = [{} for _ in range(len(pattern) + 1)]

    # initialize the dfa table for state 0
    for ch in alphabet:
        dfa[0][ch] = 0
    dfa[0][pattern[0]] = 1

    x = 0  # current restart state
    
    for q in range(1, len(pattern)):
        for ch in alphabet:
            dfa[q][ch] = dfa[x][ch]
        dfa[q][pattern[q]] = q + 1
        x = dfa[x][pattern[q]]

    for ch in alphabet:
        dfa[-1][ch] = len(pattern)

    return dfa

def generate_latex_dfa_table(dfa: list[dict[str, int]]) -> str:
    alphabet = sorted(list(dfa[0].keys()))
    print(f"alphabet: {alphabet}")
    str = "\\begin{tabular}{c|" + "c" * len(dfa) + "}\n"
    str += "  & " + " & ".join([f"${i}$" for i in range(len(dfa))]) + "\\\\\n"

    for ch in alphabet:
        line = ""
        line += f"{ch} & "
        line += " & ".join([f"${dfa[i][ch]}$" for i in range(len(dfa))]) + "\\\\\n"
        str += line

    str += "\\end{tabular}"


    return str  

## TODO: fix this to deal with the case where the pattern is matched and we continue reading the text
def kmp_failure_array(pattern: str) -> list[int]:
    failure_array = [0] * len(pattern)
    x = 0
    for j in range(1, len(pattern)):
        failure_array[j] = x
        while pattern[x] != pattern[j]:
            if x == 0:
                x = -1
                break
            else:
                x = failure_array[x]
        x += 1
    return failure_array

# returns the states of the KMP failure link automaton after processing each character in the text
def apply_kmp(pattern: str, text: str) -> list[int]:
    failure_array = kmp_failure_array(pattern)
    result = []
    states = [0] * (len(text))
    j = 0 # current index in pattern
    i = 0 # current index in text
    while i < len(text):
        if text[i] == pattern[j]:
            j += 1
            states[i] = j
            i += 1
            if j == len(pattern):
                result.append(i - len(pattern) + 1)
                j = failure_array[j-1]
        else:
            if j > 0:
                j = failure_array[j]
                states[i] = j
            else:
                i += 1
    return states

# generate an example of applying the KMP failure link automaton to a text
def generate_kmp_example(alphabet_size: int = 3, text_length: int = 20, pattern_length: int = 6, min_matches: int = 3) -> tuple[str, str, list[int]]:
    
    alphabet = [chr(i) for i in range(ord('A'), ord('A') + alphabet_size)]
    pattern = ''.join(random.choices(alphabet, k=pattern_length))
    text = ''.join(random.choices(alphabet, k=text_length))
    states = apply_kmp(pattern, text)

    while (max(states[text_length//2:]) < min_matches):
        pattern = ''.join(random.choices(alphabet, k=pattern_length))
        text = ''.join(random.choices(alphabet, k=text_length))
        states = apply_kmp(pattern, text)

    return pattern, text, states

def apply_dfa(dfa: list[dict[str, int]], text: str) -> list[int]:
    result = []
    state = 0
    for i, ch in enumerate(text):
        state = dfa[state][ch]
        result.append(state)
    return result

def print_dfa_table(dfa: list[dict[str, int]]) -> None:
    for i, state in enumerate(dfa):
        print(f"{i}: {state}")

def generate_failure_array_example(alphabet_size: int = 3, pattern_length: int = 10, min_matches: int = 3) -> tuple[str, list[int]]:
    alphabet = [chr(i) for i in range(ord('A'), ord('A') + alphabet_size)]
    matches = 0
    while matches < min_matches:
        pattern = ''.join(random.choices(alphabet, k=pattern_length))
        failure_array = kmp_failure_array(pattern)
        matches = max(failure_array)
    return pattern, failure_array

def generate_kmp_failure_array_examples(alphabet_size: int = 3, string_length: int = 10, min_matches: int = 3, num_examples: int = 10) -> None:
    for i in range(num_examples):
        pattern, failure_array = generate_failure_array_example(alphabet_size, string_length, min_matches)

        # make sure there is at least one match in the second half of the array
        while (sum(failure_array[len(failure_array)//2:]) == 0):
            pattern, failure_array = generate_failure_array_example(alphabet_size, string_length, min_matches)

        # choose an index in second half of failure_array with probability proportional to the value at the index
        index = random.choices(range(len(failure_array)//2, len(failure_array)), weights=failure_array[len(failure_array)//2:], k=1)[0]
        print(f"Example {i+1}:")
        print(f"pattern: {pattern}")
        print(f"failure array: {failure_array}")
        print(f"index: {index}")
        print(f"failure array at index: {failure_array[index]}\n")

def generate_kmp_state_examples(num_examples: int = 10) -> None:
    for i in range(num_examples):
        pattern, text, states = generate_kmp_example(alphabet_size=3, text_length=16, pattern_length=6, min_matches=3)

        # pick a random index at state at least 2 with higher states more likely
        heavy_states = [max(0, states[i]-1) for i in range(0, len(states))]
        index = random.choices(range(0, len(heavy_states)), weights=heavy_states, k=1)[0]

        print(f"Example {i+1}:")
        print(f"pattern: {pattern}")
        print(f"text: {text}")
        print(f"states: {states}")
        print(f"index: {index}")
        print(f"state at index: {states[index]}\n")


if __name__ == "__main__":
    pattern = "BARBARABARBS"
    kmp = kmp_failure_array(pattern)
    print(f"pattern: {pattern}")
    print(f"failure array: {kmp}")
    dfa = generate_dfa_table(pattern)
    print(f"pattern: {pattern}")
    print_dfa_table(dfa)

    # generate_kmp_failure_array_examples()

    # generate_kmp_state_examples()

    # pattern = "BACBAB"
    # kmp = kmp_failure_array(pattern)
    # text = "BACBAACBCCCB"
    # states = apply_kmp(pattern, text)
    # print(f"text: {text}")
    # print(f"pattern: {pattern}")
    # print(f"failure array: {kmp}")
    # print(f"states: {states}")

    # pattern = "ABABAB"
    # kmp = kmp_failure_array(pattern)
    # text = "ABABABABC"
    # states = apply_kmp(pattern, text)
    # print(f"text: {text}")
    # print(f"pattern: {pattern}")
    # print(f"failure array: {kmp}")
    # print(f"states: {states}")



    #print(kmp_failure_array("BCCCBCCBCB"))

    # print(f"latex dfa table:\n{generate_latex_dfa_table(dfa)}")

    # text = "ABABACABABACADBABABACADABAABAB"
    # result = apply_dfa(dfa, text)
    # print(f"text: {text}")
    # print(result)
