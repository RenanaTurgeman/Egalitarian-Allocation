# def egalitarian_allocation(valuations: list[list[float]]):

def egalitarian_allocation(valuations: list[list[float]]):
    n = len(valuations[0])  # number of stuff
    states = [([0, 0], 0)]
    new_states = [([0, 0], 0)]

    for state in new_states:
        current_state, level = new_states.pop()

        # in case that p1 get the stuff
        new_state_p1 = [current_state[0] + valuations[0][level], current_state[1]]
        if ((new_state_p1, level + 1) not in states)  \
                and optimal_division(valuations, states, n) >= pessimistic_division(valuations, states, n):
            states.append((new_state_p1, level + 1))
            new_states.append((new_state_p1, level + 1))

        # in case that p2 get the staff
        new_state_p2 = [current_state[0], current_state[1] + valuations[1][level]]
        if (new_state_p2, level + 1) not in states \
                and optimal_division(valuations, states, n) >= pessimistic_division(valuations, states, n):
            states.append((new_state_p2, level + 1))
            new_states.append((new_state_p2, level + 1))


def optimal_division(valuations: list[list[float]], states: [list[float], int], num: int) -> float:
    current_state, level = states.pop()
    sum1, sum2 = 0
    for stuff in range(num - level):
        sum1 += valuations[0][stuff + level]
        sum2 += valuations[1][stuff + level]
    return min(sum1, sum2)


def pessimistic_division(valuations: list[list[float]], states: [list[float], int], num: int) -> float:
    current_state, level = states.pop()
    min_value = float('inf')  # Initialize with positive infinity
    for stuff in range(num - level):
        if min_value > valuations[0][stuff + level]:
            min_value = valuations[0][stuff + level]
        if min_value > valuations[1][stuff + level]:
            min_value = valuations[1][stuff + level]
    return min_value


if __name__ == '__main__':
    egalitarian_allocation([[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]])
