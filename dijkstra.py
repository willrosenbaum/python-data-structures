import heapq

class WeightedGraph:
    def __init__(self):
        self.vertices = []
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.vertices.append(vertex)
        self.adjacency_list[vertex] = []

    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

def generate_example_graph() -> WeightedGraph:
    graph = WeightedGraph()
    for i in range(1, 8):
        graph.add_vertex(i)
    graph.add_edge(1, 3, 1.2)
    graph.add_edge(1, 4, 5.3)
    graph.add_edge(1, 6, 2.4)
    graph.add_edge(3, 6, 2.7)
    graph.add_edge(3, 2, 1.1)
    graph.add_edge(6, 5, 2.2)
    graph.add_edge(2, 4, 1.7)
    graph.add_edge(2, 7, 3.1)
    graph.add_edge(5, 4, 0.8)
    graph.add_edge(5, 7, 3.4)
    return graph

def generate_example_graph_alt() -> WeightedGraph:
    graph = WeightedGraph()
    for i in range(1, 8):
        graph.add_vertex(i)
    graph.add_edge(1, 2, 1.8)
    graph.add_edge(1, 3, 4.3)
    graph.add_edge(1, 5, 3.2)
    graph.add_edge(1, 6, 1.3)
    graph.add_edge(2, 6, 0.7)
    graph.add_edge(2, 7, 1.1)
    graph.add_edge(3, 4, 1.1)
    graph.add_edge(3, 7, 0.8)
    graph.add_edge(4, 5, 4.7)
    return graph

if __name__ == "__main__":
    graph = generate_example_graph_alt()
    print(graph.dijkstra(1))