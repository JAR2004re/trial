class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1
    def is_safe(self, v, color, colors):
        for i in range(self.vertices):
            if self.adjacency_matrix[v][i] == 1 and colors[i] == color:
                return False
        return True
    def graph_coloring(self):
        colors = [-1] * self.vertices
        colors[0] = 0
        for v in range(1, self.vertices):
            available_colors = [True] * self.vertices
            for i in range(self.vertices):
                if self.adjacency_matrix[v][i] == 1 and colors[i] != -1:
                    available_colors[colors[i]] = False
            for color in range(self.vertices):
                if available_colors[color]:
                    colors[v] = color
                    break
        print("Vertex   Color")
        for v in range(self.vertices):
            print(f"{v}\t   {colors[v]}")
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.graph_coloring()