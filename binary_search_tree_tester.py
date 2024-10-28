import random
from binary_search_tree import BinarySearchTree

rand = random.Random()

def generate_examples(num_examples):
    examples = []
    while len(examples) < num_examples:
        values = list(range(1, 11))
        rand.shuffle(values)
        tree = BinarySearchTree()
        for value in values:
            tree.insert(value)
        unbalanced_values = tree.get_unbalanced_values()
        if(len(unbalanced_values) == 3):
            examples.append([values, unbalanced_values])
    return examples

examples = generate_examples(10)
for i in range(len(examples)):
    print('Example ', i)
    print('     Original list:', examples[i][0])
    print('     Unbalanced values:', examples[i][1])

