import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, state, level):
        self.state = state
        self.level = level
        self.left = None
        self.right = None

def egalitarian_allocation(valuations: list[list[float]]):
    start_time = time.time()

    n = len(valuations[0])  # number of stuff
    root = Node([0, 0], 0)
    states = [root]
    new_states = [root]

    while new_states:
        current_node = new_states.pop()
        level = current_node.level

        if level < n:
            # in case that p1 gets the stuff
            new_state_p1 = Node([current_node.state[0] + valuations[0][level], current_node.state[1]], level + 1)
            if new_state_p1 not in states:
                states.append(new_state_p1)
                new_states.append(new_state_p1)
                current_node.left = new_state_p1

            # in case that p2 gets the staff
            new_state_p2 = Node([current_node.state[0], current_node.state[1] + valuations[1][level]], level + 1)
            if new_state_p2 not in states:
                states.append(new_state_p2)
                new_states.append(new_state_p2)
                current_node.right = new_state_p2

    # An array that contains the final states in which all stuff were divided
    filtered_states = [node for node in states if node.level == n]
    best_state = max(filtered_states, key=lambda x: min(x.state))
    end_time = time.time()
    running_time = end_time - start_time
    print_allocation(best_state, valuations)
    print(best_state.state)
    return best_state.state

def print_allocation(node, valuations):
    allocation_details = []
    current_node = node

    while current_node:
        level = current_node.level
        items = [i for i in range(len(valuations[0])) if current_node.state[0] >= valuations[0][i] and current_node.state[1] >= valuations[1][i]]
        player_value = min(current_node.state)
        allocation_details.append((level % 2, items, player_value))
        current_node = current_node.left if current_node.left and min(current_node.left.state) > min(current_node.right.state) else current_node.right

    allocation_details.reverse()

    for level, (player, items, value) in enumerate(allocation_details):
        items_str = ', '.join(map(str, items))
        print(f"Player {player} gets items {items_str} with value {value}")


# Example usage
if __name__ == '__main__':
    egalitarian_allocation([[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]])
