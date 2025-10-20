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

heap.insert(0, print_steps=False)

# sample n_values distinct values from 1 to 99:
n_values = 8
values = rand.sample(range(1, 100), n_values)
print('Sample:', values)

heap = BinaryMinHeap()
for value in values:
    heap.insert(value, print_steps=False)

print('Heap contents:', heap.heap)