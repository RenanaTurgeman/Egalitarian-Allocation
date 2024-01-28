import random


def mul_egalitarian_allocation(valuations: list[list[float]]):
    n = len(valuations[0])  # number of stuff
    states = [([0, 0], 0)]
    new_states = [([0, 0], 0)]

    while new_states:
        # print("new_states", new_states)
        # print("states", states)
        current_state, level = new_states.pop()
        max_pessimistic = 0
        if level < n:
            # in case that p1 get the stuff
            new_state_p1 = [current_state[0] + valuations[0][level], current_state[1]]
            pessimistic = pessimistic_division(valuations, states.copy()) + current_state[0]
            if pessimistic > max_pessimistic:
                max_pessimistic = pessimistic
            if ((new_state_p1, level + 1) not in states) \
                    and optimal_division(valuations, states.copy()) + current_state[0] >= max_pessimistic:
                states.append((new_state_p1, level + 1))
                new_states.append((new_state_p1, level + 1))

            # in case that p2 get the staff
            new_state_p2 = [current_state[0], current_state[1] + valuations[1][level]]
            pessimistic = pessimistic_division(valuations, states.copy()) + current_state[1]
            if pessimistic > max_pessimistic:
                max_pessimistic = pessimistic
            if (new_state_p2, level + 1) not in states \
                    and optimal_division(valuations, states.copy()) + current_state[1] >= max_pessimistic:
                states.append((new_state_p2, level + 1))
                new_states.append((new_state_p2, level + 1))
                # print(states)

    # An array that contains the final states in which all stuff were divided
    filtered_states = [state for state in states if state[1] == n]
    # print(states)
    print(max(filtered_states, key=lambda x: x[0][0] * x[0][1]))
    return max(filtered_states, key=lambda x: x[0][0] * x[0][1])


# in the optimal_division and the pessimistic_division I don't add the value the students already have, because this
# amount will be reduced when compared
def optimal_division(valuations: list[list[float]], states: [list[float], int]) -> float:
    num = len(valuations[0])  # number of stuff
    current_state, level = states.pop()
    sum_value_p1, sum_value_p2 = 0, 0
    for stuff in range(num - level):
        sum_value_p1 += valuations[0][stuff + level]
        sum_value_p2 += valuations[1][stuff + level]
    return min(sum_value_p1, sum_value_p2)


def pessimistic_division(valuations: list[list[float]], states: [list[float], int]) -> float:
    num = len(valuations[0])  # number of stuff
    if not states:
        # Handle the case when the list is empty
        return 0

    current_state, level = states.pop()
    sum_value_p1, sum_value_p2 = 0, 0
    for stuff in range(num - level):  # Go over the remaining stuff
        rnd = random.randint(0, 10)  # for give the remaining stuff by random
        if rnd < 5:  # If the number drawn is less than 5, the first student will receive it
            sum_value_p1 += valuations[0][stuff + level]
        else:  # else, the second student will receive it
            sum_value_p2 += valuations[1][stuff + level]
    return min(sum_value_p1, sum_value_p2)


# def print_allocation(result, valuations):
#     final_state, level = result
#
#     # is_all_zero = False
#     # while not is_all_zero:
#     #
#
#     # Create a list to store allocation details for each player
#     allocation_details = []
#
#     # TODO: FIX IT
#     # Iterate over each player and their corresponding values in the final_state
#     for player, value in enumerate(final_state):
#         allocated_items = [i for i in range(len(valuations[player]))]
#         player_value = value
#         allocation_details.append((player, allocated_items, player_value))
#
#     allocation_details.reverse()
#
#     for level, (player, items, value) in enumerate(allocation_details):
#         items_str = ', '.join(map(str, items))
#         print(f"Player {player} gets items {items_str} with value {value}")


if __name__ == '__main__':
    mul_egalitarian_allocation([[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]])
    mul_egalitarian_allocation([[4, 5, 6, 7], [8, 7, 6, 5]])
    mul_egalitarian_allocation([[4, 5], [8, 7]])
    mul_egalitarian_allocation([[6, 7, 9], [9, 7, 6]])

    valuations = [[4, 5], [8, 7]]
    result = mul_egalitarian_allocation(valuations)  # ([5, 8], 2)
    print_allocation(result, valuations)
