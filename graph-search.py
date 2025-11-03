from typing import Any
import random



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
        print(pi)
        self.vertices = permuted_vertices
        self.adjacency_list = {pi[vertex]: [pi[neighbor] for neighbor in self.adjacency_list[vertex]] for vertex in self.vertices}

    def print_graph(self) -> None:
        for vertex in self.vertices:
            print(f"{vertex}: {self.adjacency_list[vertex]}")
        
    def bfs(self, start):
        visited = set[Any]()
        queue = [start]
        visited.add(start)
        while queue:
            current = queue.pop(0)
            print(current)
            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start):
        visited = []
        stack = [start]
        while stack:
            current = stack.pop()
            if not current in visited:
                visited.append(current)
                print(str(current) + ", ")
                for neighbor in reversed(self.adjacency_list[current]):
                    stack.append(neighbor)

if __name__ == "__main__":
    graph = Graph()
    for i in range(6):
        graph.add_vertex(i+1)
    graph.adjacency_list[1] = [2, 4]
    graph.adjacency_list[2] = [5, 3, 1]
    graph.adjacency_list[3] = [4, 2]
    graph.adjacency_list[4] = [1, 3, 5, 6]
    graph.adjacency_list[5] = [4, 2, 6]
    graph.adjacency_list[6] = [4, 5]
    graph.print_graph()
    graph.dfs(1)
    graph.permute_ids()
    graph.print_graph()
    graph.dfs(1)