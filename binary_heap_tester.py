from binary_heap import BinaryMinHeap
from random import *

rand = Random()
values = list(range(1,9))
rand.shuffle(values)

heap = BinaryMinHeap()
for value in values:
    heap.insert(value)

print('Original list:', values)
print('Heap contents:', heap.heap)

trio = [heap.heap[0], heap.heap[1], heap.heap[3]]
print('Trio:', trio)

removed = []
while heap.size() > 0:
    removed.append(heap.extract_min())

print('Removed:', removed)

