import random
import time
import matplotlib.pyplot as plt

# Graph the running time of your function as a function of the number of objects, when using both
# The pruning rules we learned in the lecture, or only in rule A, or only in rule B, or in none of the rules.
# I created a function for each of the rules,
# I deleted the printing functions because it is not important here, and I calculated running times for each of them


def egalitarian_allocation_with2rules(valuations: list[list[float]]):
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

    return final_state


def egalitarian_allocation_with_first_rule(valuations: list[list[float]]):
    # with the rule of delete identical states
    n = len(valuations[0])  # number of stuff
    states = [([0, 0], 0, None)]  # Add None as the initial parent for the root state
    new_states = [([0, 0], 0, None)]

    while new_states:
        current_state, level, parent_state = new_states.pop()
        if level < n:

            # in case that p1 get the stuff
            # Calculate the new state:
            new_state_p1 = [current_state[0] + valuations[0][level], current_state[1]]

            # Checks the first rule:
            if (new_state_p1, level + 1, current_state) not in states:
                states.append((new_state_p1, level + 1, current_state))
                new_states.append((new_state_p1, level + 1, current_state))

            # in case that p2 get the staff
            # Calculate the new state:
            new_state_p2 = [current_state[0], current_state[1] + valuations[1][level]]

            # Checks the first rule:
            if (new_state_p2, level + 1, current_state) not in states:
                states.append((new_state_p2, level + 1, current_state))
                new_states.append((new_state_p2, level + 1, current_state))

    # An array that contains the final states in which all stuff were divided
    filtered_states = [state for state in states if state[1] == n]
    final_state = max(filtered_states, key=lambda x: min(x[0]))

    return final_state


def egalitarian_allocation_without_rules(valuations: list[list[float]]):
    n = len(valuations[0])  # number of stuff
    states = [([0, 0], 0, None)]  # Add None as the initial parent for the root state
    new_states = [([0, 0], 0, None)]

    while new_states:
        current_state, level, parent_state = new_states.pop()
        if level < n:
            # in case that p1 get the stuff
            # Calculate the new state:
            new_state_p1 = [current_state[0] + valuations[0][level], current_state[1]]

            states.append((new_state_p1, level + 1, current_state))
            new_states.append((new_state_p1, level + 1, current_state))

            # in case that p2 get the staff
            # Calculate the new state:
            new_state_p2 = [current_state[0], current_state[1] + valuations[1][level]]

            states.append((new_state_p2, level + 1, current_state))
            new_states.append((new_state_p2, level + 1, current_state))

    # An array that contains the final states in which all stuff were divided
    filtered_states = [state for state in states if state[1] == n]
    final_state = max(filtered_states, key=lambda x: min(x[0]))

    return final_state


def egalitarian_allocation_with_second_rule(valuations: list[list[float]]):
    # with pruning rule
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
            if optimal_division(valuations, states.copy()) + current_state[0] >= max_pessimistic:
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
            if optimal_division(valuations, states.copy()) + current_state[1] >= max_pessimistic:
                states.append((new_state_p2, level + 1, current_state))
                new_states.append((new_state_p2, level + 1, current_state))

    # An array that contains the final states in which all stuff were divided
    filtered_states = [state for state in states if state[1] == n]
    final_state = max(filtered_states, key=lambda x: min(x[0]))

    return final_state


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


def measure_running_time(valuations_function, valuations):
    start_time = time.time()
    valuations_function(valuations)
    elapsed_time = time.time() - start_time
    return elapsed_time


if __name__ == '__main__':

    valuations_list = [
        [[4, 5], [8, 7]],  # 2

        [[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]],  # 5

        [[4, 5, 6, 7, 8, 7, 4], [8, 7, 6, 5, 4, 5, 9]],  # 7

        [[4, 5, 6, 7, 8, 6, 7, 8, 9, 2], [8, 7, 6, 5, 4, 4, 5, 6, 7, 8]],  # 10

        [[4, 5, 6, 7, 8, 6, 7, 8, 9, 2, 4, 6], [8, 7, 6, 5, 4, 4, 5, 6, 7, 8, 3, 4]],  # 12

        [[4, 5, 6, 7, 8, 6, 7, 8, 9, 2, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8]],  # 15

        [[4, 5, 6, 7, 8, 6, 7, 8, 9, 2, 4, 5, 5, 4, 6, 7, 8], [8, 7, 6, 5, 4, 7, 8, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8]],
        # 17

        [[4, 5, 6, 7, 8, 6, 7, 8, 9, 2, 4, 5, 6, 7, 8, 2, 4, 1, 9, 5],
         [8, 7, 6, 5, 4, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 6, 1, 9, 1, 5]],  # 20

        [[4, 5, 6, 7, 8, 6, 7, 8, 9, 2, 4, 5, 6, 7, 8, 2, 4, 1, 9, 5, 4, 5, 6, 7, 8],
         [4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 6, 1, 9, 1, 5]],

    ]

    num_products = [2, 5, 7, 10, 12, 15, 17, 20, 25]

    functions = [
        egalitarian_allocation_with2rules,
        egalitarian_allocation_with_first_rule,
        egalitarian_allocation_with_second_rule,
        egalitarian_allocation_without_rules,
    ]

    for function in functions:
        times = []

        for valuations in valuations_list:
            elapsed_time = measure_running_time(function, valuations)
            times.append(elapsed_time)
        print("done")
        # Extract x and y values from product_time
        x_values = num_products
        y_values = times

        # Plot the graph
        plt.plot(x_values, y_values, marker='o', linestyle='-')
        plt.title('Running Time vs. Input Size')
        plt.xlabel('Input Size')
        plt.ylabel('Running Time (seconds)')
        plt.grid(True)
        plt.show()

