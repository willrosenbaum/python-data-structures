from binary_heap import BinaryMinHeap
from random import *

rand = Random()
values = list(range(1,8))
rand.shuffle(values)

heap = BinaryMinHeap()
for value in values:
    heap.insert(value)

print('Original list:', values)
print('Heap contents:', heap.heap)
print('Inserting the value 0')

heap.insert(0, print_steps=True)

