class HuffmanNode:
    def __init__(self, symbol: str, weight: int, left: 'HuffmanNode' = None, right: 'HuffmanNode' = None):
        self.symbol = symbol # store the smallest symbol in the subtree
        self.weight = weight
        self.left = left
        self.right = right
    
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None
    
    def __lt__(self, other: 'HuffmanNode') -> bool:
        if self.weight == other.weight:
            return ord(self.symbol) < ord(other.symbol)
        return self.weight < other.weight
    
    def get_code(self, code: dict[str, str], prefix: str = '') -> dict[str, str]:
        if self.is_leaf():
            code[self.symbol] = prefix
        else:
            self.left.get_code(code, prefix + '0')
            self.right.get_code(code, prefix + '1')
        return code

class HuffmanTree:
    def __init__(self, root: HuffmanNode):
        self.root = root

    def get_code(self) -> dict[str, str]:
        code = {}
        return dict(sorted(self.root.get_code(code, '').items()))
    
    def encode(self, message: str) -> str:
        code = self.get_code()
        return ''.join(code[symbol] for symbol in message)
    
    def decode(self, encoded_message: str) -> str:
        decoded_message = ''
        current_node = self.root
        for bit in encoded_message:
            current_node = current_node.left if bit == '0' else current_node.right
            if current_node.is_leaf():
                decoded_message += current_node.symbol
                current_node = self.root
        return decoded_message
    
    @staticmethod
    def build_huffman_tree(weights: dict[str, int]) -> 'HuffmanTree':
        nodes = [HuffmanNode(symbol, weight) for symbol, weight in weights.items()]
        while len(nodes) > 1:
            nodes.sort()
            left = nodes.pop(0)
            right = nodes.pop(0)
            nodes.append(HuffmanNode(min(left.symbol, right.symbol), left.weight + right.weight, left, right))
        return HuffmanTree(nodes[0])
    
def compute_frequency_count(word: str) -> dict[str, int]:
    counts = {letter: word.count(letter) for letter in set(word)}
    return dict(sorted(counts.items()))

# 10 letter words with only 5 distinct letters
words = [
    'ADDRESSEES',
    'ASSESSABLE',
    'BANANALAND',
    'BASENESSES',
    'DEADPANNED',
    'FOOTSTOOLS',
    'HALLABALOO',
    'IFFINESSES',
    'KNICKKNACK',
    'REASSESSED',
    'SELFLESSLY',
    'STATISTICS',
    'UNDEADENED',
    'UNEVENNESS',
    'UNSONOROUS',
    'WELLNESSES',
    'ZIGZAGGING'
]


if __name__ == '__main__':
    """
    Given the alphabet Σ= {E, L, N, P, S}with frequencies
E : 4, L : 2, N : 1, P : 1, S : 5
    construct the Huffman code for Σ and use it to decode the following coded text:
    011010101111110100011101000
    """
    # weights = {'E': 4, 'L': 2, 'N': 1, 'P': 1, 'S': 5}
    # tree = HuffmanTree.build_huffman_tree(weights)
    # print(tree.get_code())
    # #encoded_message = tree.encode('ENLPS')
    # encoded_message = '011010101111110100011101000'
    # #print(encoded_message)
    # decoded_message = tree.decode(encoded_message)
    # print(f'Decoded message: {decoded_message}')

    count = 1
    for word in words:
        print(f'Example: {count}')
        print(f'Word: {word}')
        weights = compute_frequency_count(word)
        print(f'Distinct letters: {sorted(list(weights.keys()))}'.replace("'", "").replace('[', '{').replace(']', '}'))
        print(f'Weights: {weights}'.replace("'", ""))
        tree = HuffmanTree.build_huffman_tree(weights)
        print(f'Code: {tree.get_code()}')
        print(f'Encoded message: {tree.encode(word)}')
        print(f'Decoded message: {tree.decode(tree.encode(word))}\n')
        count += 1

