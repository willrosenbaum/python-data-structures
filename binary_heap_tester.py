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

# sample 15 distinct values from 1 to 99:
values = rand.sample(range(1, 100), 15)
print('Sample:', values)

heap = BinaryMinHeap()
for value in values:
    heap.insert(value, print_steps=True)

print('Heap contents:', heap.heap)