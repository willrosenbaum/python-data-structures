class BinaryMinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value: int):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)

    def bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.bubble_up(parent_index)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.trickle_down(0)
        return min_value
    
    def trickle_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_child_index = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[left_child_index]:
            smallest_child_index = right_child_index
        if smallest_child_index < len(self.heap) and self.heap[smallest_child_index] < self.heap[index]:
            self.heap[index], self.heap[smallest_child_index] = self.heap[smallest_child_index], self.heap[index]
            self.trickle_down(smallest_child_index)

    def size(self):
        return len(self.heap)
    
    