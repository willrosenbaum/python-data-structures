from typing import Any
import random
import copy

random.seed(1)

def stringify_list(list: list) -> str:
    return ', '.join(str(item) for item in list)

def contains_duplicate(list: list) -> bool:
    return len(list) != len(set(list))

class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacency_list = {}

    def add_vertex(self, vertex) -> None:
        self.vertices.append(vertex)
        self.adjacency_list[vertex] = []

    def add_edge(self, u, v) -> None:
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def permute_ids(self) -> None:
        permuted_vertices = self.vertices.copy()
        random.shuffle(permuted_vertices)
        pi = {self.vertices[i]: permuted_vertices[i] for i in range(len(self.vertices))}
        #print(pi)
        self.vertices = permuted_vertices
        self.adjacency_list = {pi[vertex]: [pi[neighbor] for neighbor in self.adjacency_list[vertex]] for vertex in self.vertices}
        return pi

    def print_graph(self) -> None:
        vertices = sorted(self.vertices)
        for i in range(len(vertices)):
            v = vertices[i]
            neighbors = self.adjacency_list[v]
            print(f"{v}: {stringify_list(neighbors)}")
                
    def bfs(self, start):
        visited = []
        queue = [start]
        visited.append(start)
        while queue:
            current = queue.pop(0)
            #print(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return visited

    def dfs(self, start):
        visited = []
        stack = [start]
        while stack:
            current = stack.pop()
            if not current in visited:
                visited.append(current)
                # print(str(current))
                for neighbor in reversed(self.adjacency_list[current]):
                    stack.append(neighbor)
        return visited

    def reversed_dfs(self, start):
        visited = []
        stack = [start]
        while stack:
            current = stack.pop()
            if not current in visited:
                visited.append(current)
                # print(str(current))
                for neighbor in self.adjacency_list[current]:
                    stack.append(neighbor)
        return visited

    def stack_search(self, start):
        visited = [start]
        stack = [start]
        while stack:
            current = stack.pop()
            #print(current)
            for neighbor in reversed(self.adjacency_list[current]):
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)
        return visited

    def reversed_stack_search(self, start):
        visited = [start]
        stack = [start]
        while stack:
            current = stack.pop()
            #print(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)
        return visited

    def reversed_bfs(self, start):
        visited = [start]
        queue = [start]
        while queue:
            current = queue.pop(0)
            #print(current)
            for neighbor in reversed(self.adjacency_list[current]):
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return visited

def generate_example_graph() -> Graph:
    graph = Graph()
    for i in range(7):
        graph.add_vertex(i+1)
    graph.adjacency_list[1] = [3, 2]
    graph.adjacency_list[2] = [3, 6, 1, 7]
    graph.adjacency_list[3] = [1, 6, 2, 5, 4]
    graph.adjacency_list[4] = [5, 3]
    graph.adjacency_list[5] = [3, 4]
    graph.adjacency_list[6] = [2, 3, 7]
    graph.adjacency_list[7] = [6, 2]
    return graph

def generate_larger_example_graph() -> Graph:
    graph = Graph()
    for i in range(1, 9):
        graph.add_vertex(i)
    graph.adjacency_list[1] = [8, 7, 3]
    graph.adjacency_list[2] = [3, 7, 5]
    graph.adjacency_list[3] = [7, 1, 2]
    graph.adjacency_list[4] = [6, 5]
    graph.adjacency_list[5] = [2, 6, 4]
    graph.adjacency_list[6] = [5, 4]
    graph.adjacency_list[7] = [8, 1, 2, 3]
    graph.adjacency_list[8] = [7, 1]
    return graph

def generate_new_example(graph: Graph, start: Any, permute_ids: bool = True):
    g = copy.deepcopy(graph)
    if permute_ids: 
        pi = g.permute_ids()
    else:
        pi = {g.vertices[i]: g.vertices[i] for i in range(len(g.vertices))}
    print('ID permutation:', pi)
    print(f'Consider the graph G = (V, E) with vertex set V = {{{stringify_list(sorted(g.vertices))}}} represented by the following adjacency lists:')
    g.print_graph()
    print(f'Given a starting vertex u = {pi[start]}, in what order are the vertices visited according to the Depth-first Search (DFS) starting from vertex {pi[start]}?')
    possible_answers = [stringify_list(g.dfs(pi[start])), 
                    stringify_list(g.reversed_dfs(pi[start])), 
                    stringify_list(g.bfs(pi[start])), 
                    stringify_list(g.stack_search(pi[start])), 
                    stringify_list(g.reversed_stack_search(pi[start])), 
                    stringify_list(g.reversed_bfs(pi[start]))]
    methods = ['DFS', 'Reversed DFS', 'BFS', 'Stack search', 'Reversed stack search', 'Reversed BFS']
    for i in range(len(methods)):
        print(f'{methods[i]}: {possible_answers[i]}')
    if contains_duplicate(possible_answers):
        print('Error: contains duplicates')
    else:
        print('No duplicate answers')

    

if __name__ == "__main__":
    # graph = generate_example_graph()
    # generate_new_example(graph, 1, False)
    # for i in range(1, 8):
    #     print(f'Example {i}:')
    #     generate_new_example(graph, 1, True)
    #     print('\n\n\n')
    graph = generate_larger_example_graph()
    generate_new_example(graph, 1, False)