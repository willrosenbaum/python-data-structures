
class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_end_of_word = False

    def add_child(self, child):
        self.children.append(child)

    def is_leaf(self):
        return len(self.children) == 0

class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        current_node = self.root
        for char in word:
            if current_node.children.contains_key(char):
                current_node = current_node.children[char]
            else:
                current_node.children[char] = TrieNode(char)
                current_node = current_node.children[char]
        current_node.is_end_of_word = True
