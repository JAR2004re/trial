class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target_amount):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target_amount = target_amount
        self.visited_states = set()
    def pour(self, state, action):
        jug1, jug2 = state
        new_state = None
        if action == 'fill jug1':
            new_state = (self.jug1_capacity, jug2)
        elif action == 'fill jug2':
            new_state = (jug1, self.jug2_capacity)
        elif action == 'empty jug1':
            new_state = (0, jug2)
        elif action == 'empty jug2':
            new_state = (jug1, 0)
        elif action == 'pour jug1 to jug2':
            amount_to_pour = min(jug1, self.jug2_capacity - jug2)
            new_state = (jug1 - amount_to_pour, jug2 + amount_to_pour)
        elif action == 'pour jug2 to jug1':
            amount_to_pour = min(jug2, self.jug1_capacity - jug1)
            new_state = (jug1 + amount_to_pour, jug2 - amount_to_pour)
        return new_state
    def is_goal_state(self, state):
        return self.target_amount in state
    def print_solution(self, path):
        for i, state in enumerate(path):
            print(f"Step {i}: Jug1={state[0]}, Jug2={state[1]}")
    def solve(self):
        initial_state = (0, 0)
        frontier = [(initial_state, [])]
        while frontier:
            state, path = frontier.pop(0)
            self.visited_states.add(state)
            if self.is_goal_state(state):
                print("Solution found!")
                self.print_solution(path)
                break
            for action in ['fill jug1', 'fill jug2', 'empty jug1', 'empty jug2', 'pour jug1 to jug2', 'pour jug2 to jug1']:
                new_state = self.pour(state, action)
                if new_state not in self.visited_states:
                    frontier.append((new_state, path + [new_state]))
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2
problem = WaterJugProblem(jug1_capacity, jug2_capacity, target_amount)
problem.solve()