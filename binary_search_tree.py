class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        new_node = BSTNode(value)
        if value < node.value:
            if node.left is None:
                node.left = new_node
                new_node.parent = node
                self._update_height(node)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = new_node
                new_node.parent = node
                self._update_height(node)   
            else:
                self._insert(value, node.right)

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        if node.parent is not None:
            self._update_height(node.parent)    

    def _height(self, node):
        if node is None:
            return -1
        else:
            return node.height
        
    def _is_balanced(self, node):
        if node is None:
            return True
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return abs(left_height - right_height) <= 1
    
    def is_balanced(self):
        return self._is_balanced(self.root)
    
    def get_unbalanced_values(self):
        unbalanced_values = []
        self._get_unbalanced_values(self.root, unbalanced_values)
        return unbalanced_values

    def _get_unbalanced_values(self, node, unbalanced_values):
        if node is None:
            return
        self._get_unbalanced_values(node.left, unbalanced_values)
        if not self._is_balanced(node):
            unbalanced_values.append(node.value)
        self._get_unbalanced_values(node.right, unbalanced_values)

    def print_tree(self):
        print(self._to_string(self.root))

    def _to_string(self, node):
        string = ''
        if node is None:
            return string
        string += '('
        string += self._to_string(node.left)
        string += str(node.value)
        string += self._to_string(node.right)
        string += ')'
        return string