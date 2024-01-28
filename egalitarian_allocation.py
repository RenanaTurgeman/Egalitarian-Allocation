import random
import time
import matplotlib.pyplot as plt


def egalitarian_allocation(valuations: list[list[float]]):
    n = len(valuations[0])  # number of stuff
    states = [([0, 0], 0, None)]  # Add None as the initial parent for the root state
    new_states = [([0, 0], 0, None)]

    while new_states:
        current_state, level, parent_state = new_states.pop()
        max_pessimistic = 0
        if level < n:

            # in case that p1 get the stuff
            # Calculate the new state:
            new_state_p1 = [current_state[0] + valuations[0][level], current_state[1]]
            # Calculate the pessimistic_division
            pessimistic = pessimistic_division(valuations, states.copy()) + current_state[0]
            # For taking the best pessimistic block we found:
            if pessimistic > max_pessimistic:
                max_pessimistic = pessimistic

            # Checks both rules:
            if ((new_state_p1, level + 1, current_state) not in states) \
                    and optimal_division(valuations, states.copy()) + current_state[0] >= max_pessimistic:
                states.append((new_state_p1, level + 1, current_state))
                new_states.append((new_state_p1, level + 1, current_state))

            # in case that p2 get the staff
            # Calculate the new state:
            new_state_p2 = [current_state[0], current_state[1] + valuations[1][level]]
            # Calculate the pessimistic_division
            pessimistic = pessimistic_division(valuations, states.copy()) + current_state[1]
            # For taking the best pessimistic block we found:
            if pessimistic > max_pessimistic:
                max_pessimistic = pessimistic

            # Checks both rules:
            if (new_state_p2, level + 1, current_state) not in states \
                    and optimal_division(valuations, states.copy()) + current_state[1] >= max_pessimistic:
                states.append((new_state_p2, level + 1, current_state))
                new_states.append((new_state_p2, level + 1, current_state))

    # An array that contains the final states in which all stuff were divided
    filtered_states = [state for state in states if state[1] == n]
    final_state = max(filtered_states, key=lambda x: min(x[0]))

    path = find_parent(states, final_state)
    dictionary = create_results(path)
    print_results(dictionary, final_state)


def find_parent(states, target_vector):
    result = []

    for parent_state in states:
        if parent_state[0] == target_vector[2]:
            # Recursively find the parent states
            result.extend(find_parent(states, parent_state))

    return [target_vector[0]] + result


def create_results(path):
    results = {0: [], 1: []}
    staff = 0
    path.reverse() # for move from the root to the leaf
    for state, next_state in zip(path, path[1:]):
        if state[0] != next_state[0]:
            # player 0 take the current staff
            results[0].append(staff)
        elif state[1] != next_state[1]:
            # player 1 take the current staff
            results[1].append(staff)
        staff += 1

    return results


def print_results(results, target):
    for player in results:
        objects = ', '.join(map(str, results[player]))  # Convert the list to a string
        value = target[0][player]
        print(f"player {player} gets items {objects} with values {value}")


def optimal_division(valuations: list[list[float]], states: [list[float], int]) -> float:
    num = len(valuations[0])  # number of stuff
    current_state, level, parent_state = states.pop()
    sum_value_p1, sum_value_p2 = 0, 0

    # Calculate the sum of values for both players
    for stuff in range(num - level):
        sum_value_p1 += valuations[0][stuff + level]
        sum_value_p2 += valuations[1][stuff + level]

    # Return the minimum sum of values between the two players
    return min(sum_value_p1, sum_value_p2)


def pessimistic_division(valuations: list[list[float]], states: [list[float], int]) -> float:
    num = len(valuations[0])  # number of stuff
    if not states:
        # Handle the case when the list is empty
        return 0

    current_state, level, parent_state = states.pop()
    sum_value_p1, sum_value_p2 = 0, 0
    for stuff in range(num - level):  # Go over the remaining stuff
        rnd = random.randint(0, 10)  # for give the remaining stuff by random
        if rnd < 5:  # If the number drawn is less than 5, the first student will receive it
            sum_value_p1 += valuations[0][stuff + level]
        else:  # else, the second student will receive it
            sum_value_p2 += valuations[1][stuff + level]
    return min(sum_value_p1, sum_value_p2)



if __name__ == '__main__':
    egalitarian_allocation([[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]])
    # egalitarian_allocation([[4, 5, 6, 7], [8, 7, 6, 5]])
    # egalitarian_allocation([[4, 5], [8, 7]])
    # egalitarian_allocation([[6, 7, 9], [9, 7, 6]])

