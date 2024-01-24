def egalitarian_allocation(valuations):
    n = len(valuations)
    m = n  # Number of objects is assumed to be equal to the number of players

    def is_proportional(state):
        total_value = sum(state)
        for i in range(n):
            if state[i] < (valuations[i] / n) * total_value:
                return False
        return True

    def generate_children(state, t):
        children = []
        for i in range(n):
            child_state = state.copy()
            child_state[i] += valuations[i][t]
            child_state[-1] += 1
            children.append(child_state)
        return children

    def prune(state, t):
        optimistic_distribution = [(state[i] + sum(valuations[i][t:])) for i in range(n)]
        optimistic_total_value = sum(optimistic_distribution)
        optimistic_proportional_value = optimistic_total_value / n

        for i in range(n):
            if optimistic_distribution[i] < optimistic_proportional_value:
                return True
        return False

    def search_space():
        queue = [([0] * n) + [0]]  # Initial state
        while queue:
            current_state = queue.pop(0)
            t = current_state[-1]

            if t == m:
                if is_proportional(current_state):
                    yield current_state
            elif not prune(current_state, t):
                children = generate_children(current_state, t)
                queue.extend(children)

    for solution in search_space():
        player_baskets = [sum(valuations[i][t] for t in range(m) if solution[i] > 0) for i in range(n)]
        print(
            f"Player 0 gets items {', '.join(str(t) for t in range(m) if solution[0][t] > 0)} with value {player_baskets[0]}")
        print(
            f"Player 1 gets items {', '.join(str(t) for t in range(m) if solution[1][t] > 0)} with value {player_baskets[1]}")
        break  # Only print the first solution


# Example usage
egalitarian_allocation([[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]])
