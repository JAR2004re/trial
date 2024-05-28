import heapq
class PuzzleNode:
    def __init__(self, state, parent=None, move=""):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0
        self.depth = 0
        if self.parent:
            self.depth = parent.depth + 1
    def __lt__(self, other):
        return self.cost < other.cost
    def __eq__(self, other):
        return self.state == other.state
    def __hash__(self):
        return hash(str(self.state))
    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.state])
class EightPuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    def heuristic(self, state):
        total_distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    x, y = divmod(state[i][j] - 1, 3)
                    total_distance += abs(x - i) + abs(y - j)
        return total_distance
    def generate_children(self, node):
        children = []
        empty_i, empty_j = self.find_empty_space(node.state)
        for move in self.moves:
            new_i, new_j = empty_i + move[0], empty_j + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in node.state]
                new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
                child_node = PuzzleNode(new_state, parent=node, move=self.move_name(move))
                children.append(child_node)
        return children
    def find_empty_space(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
    def move_name(self, move):
        if move == (0, -1):
            return "LEFT"
        elif move == (0, 1):
            return "RIGHT"
        elif move == (-1, 0):
            return "UP"
        elif move == (1, 0):
            return "DOWN"
    def solve(self):
        initial_node = PuzzleNode(self.initial_state)
        initial_node.cost = self.heuristic(initial_node.state)
        frontier = [initial_node]
        explored = set()
        while frontier:
            node = heapq.heappop(frontier)
            if node.state == self.goal_state:
                return self.print_solution(node)
            explored.add(node)
            children = self.generate_children(node)
            for child in children:
                if child not in explored:
                    child.cost = child.depth + self.heuristic(child.state)
                    heapq.heappush(frontier, child)
    def print_solution(self, node):
        path = []
        while node.parent:
            path.append((node.move, node.state))
            node = node.parent
        path.reverse()
        for step, state in path:
            print(f"Move {step}:")
            print('\n'.join([' '.join([str(cell) for cell in row]) for row in state]))
            print()
initial_state = [
    [1, 0, 3],
    [4, 2, 6],
    [7, 5, 8]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
solver = EightPuzzleSolver(initial_state, goal_state)
solver.solve()