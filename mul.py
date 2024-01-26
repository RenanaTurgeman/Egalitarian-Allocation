import random


def mul_egalitarian_allocation(valuations: list[list[float]]):
    n = len(valuations[0])  # number of stuff
    states = [([1, 1], 0)]
    new_states = [([1, 1], 0)]

    while new_states:
        current_state, level = new_states.pop()
        if level < n:
            # in case that p1 get the stuff
            new_state_p1 = [current_state[0] * valuations[0][level], current_state[1]]
            if ((new_state_p1, level + 1) not in states) \
                    and optimal_division(valuations, states.copy()) >= pessimistic_division(valuations, states.copy()):
                states.append((new_state_p1, level + 1))
                new_states.append((new_state_p1, level + 1))

            # in case that p2 get the staff
            new_state_p2 = [current_state[0], current_state[1] * valuations[1][level]]
            if (new_state_p2, level + 1) not in states \
                    and optimal_division(valuations, states.copy()) >= pessimistic_division(valuations, states.copy()):
                states.append((new_state_p2, level + 1))
                new_states.append((new_state_p2, level + 1))

    # An array that contains the final states in which all stuff were divided
    filtered_states = [state for state in states if state[1] == n]
    print(max(filtered_states, key=lambda x: min(x[0])))
    return max(filtered_states, key=lambda x: min(x[0]))


# in the optimal_division and the pessimistic_division I don't add the value the students already have, because this
# amount will be reduced when compared
def optimal_division(valuations: list[list[float]], states: [list[float], int]) -> float:
    num = len(valuations[0])  # number of stuff
    current_state, level = states.pop()
    mul_value_p1, mul_value_p2 = 0, 0
    for stuff in range(num - level):
        mul_value_p1 *= valuations[0][stuff + level]
        mul_value_p2 *= valuations[1][stuff + level]
    return min(mul_value_p1, mul_value_p2)


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
            sum_value_p1 *= valuations[0][stuff + level]
        else:  # else, the second student will receive it
            sum_value_p2 *= valuations[1][stuff + level]
    return min(sum_value_p1, sum_value_p2)


if __name__ == '__main__':
    # egalitarian_allocation([[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]])
    # egalitarian_allocation([[4, 5, 6, 7], [8, 7, 6, 5]])
    mul_egalitarian_allocation([[4, 5], [8, 7]])
    # egalitarian_allocation([[6, 7, 9], [9, 7, 6]])
    # egalitarian_allocation([[55, 11], [44, 33]])


    # valuations = [[4, 5], [8, 7]]
    # result = egalitarian_allocation(valuations)  # ([5, 8], 2)
    # print_allocation(result, valuations)
