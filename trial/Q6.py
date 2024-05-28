import numpy as np

class GridWorldMDP:
    def __init__(self, grid_size, rewards, terminal_states, discount_factor=0.9):
        self.grid_size = grid_size
        self.rewards = rewards
        self.terminal_states = terminal_states
        self.discount_factor = discount_factor
        self.actions = ['up', 'down', 'left', 'right']
        self.policy = np.random.choice(self.actions, size=grid_size)
        self.value_function = np.zeros(grid_size)

    def is_terminal(self, state):
        return state in self.terminal_states

    def get_next_state(self, state, action):
        if self.is_terminal(state):
            return state
        x, y = state
        if action == 'up':
            x = max(0, x - 1)
        elif action == 'down':
            x = min(self.grid_size[0] - 1, x + 1)
        elif action == 'left':
            y = max(0, y - 1)
        elif action == 'right':
            y = min(self.grid_size[1] - 1, y + 1)
        return (x, y)

    def policy_evaluation(self):
        new_value_function = np.zeros(self.grid_size)
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                state = (i, j)
                action = self.policy[state]
                next_state = self.get_next_state(state, action)
                reward = self.rewards[next_state]
                new_value_function[state] = reward + self.discount_factor * self.value_function[next_state]
        self.value_function = new_value_function

    def policy_improvement(self):
        new_policy = np.copy(self.policy)
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                state = (i, j)
                if self.is_terminal(state):
                    continue
                value_action = []
                for action in self.actions:
                    next_state = self.get_next_state(state, action)
                    reward = self.rewards[next_state]
                    value_action.append(reward + self.discount_factor * self.value_function[next_state])
                best_action = self.actions[np.argmax(value_action)]
                new_policy[state] = best_action
        self.policy = new_policy

    def policy_iteration(self, max_iterations=1000):
        for i in range(max_iterations):
            old_policy = np.copy(self.policy)
            self.policy_evaluation()
            self.policy_improvement()
            if np.array_equal(old_policy, self.policy):
                break


grid_size = (3, 3)
rewards = np.full(grid_size, -0.04)
rewards[0, 2] = 1
rewards[2, 0] = -1
terminal_states = [(0, 2), (2, 0)]

mdp = GridWorldMDP(grid_size, rewards, terminal_states)
mdp.policy_iteration()

print("Optimal Policy:")
print(mdp.policy)
print("Value Function:")
print(mdp.value_function)

