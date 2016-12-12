import sys
import copy

start = [3, 3, 1]
size = 3

possible_actions = [[1, 0, 1], [2, 0, 1], [0, 1, 1], [0, 2, 1], [1, 1, 1]]

memo = []
solution = 0

def substract(vector1, vector2):
    return [vector1[i] - vector2[i] for i in range(3)]


def add(vector1, vector2):
    return [vector1[i] + vector2[i] for i in range(3)]


def valid_add(vector):
    actions = []
    for action in possible_actions:
        added = add(vector, action)
        other = substract([size, size, 1], added)
        if added[0] >= 0 and added[1] >= 0 and added[0] <= size and added[1] <= size and (added[0] >= added[1] or added[0] == 0) and (other[0] >= other[1] or other[0] == 0):
            actions.append(action)

    return actions


def valid_substract(vector):
    actions = []
    for action in possible_actions:
        substracted = substract(vector, action)
        other = substract([size, size, 1], substracted)
        if substracted[0] >= 0 and substracted[1] >= 0 and substracted[0] <= size and substracted[1] <= size and (substracted[0] >= substracted[1] or substracted[0] == 0) and (other[0] >= other[1] or other[0] == 0):
            actions.append(action)

    return actions


def solve(vector, moves, print_steps):
    global solution

    if vector in memo:
        return
    else:
        memo.append(vector)

    moves = copy.deepcopy(moves)
    moves += 1

    if vector[2] == 0:
        actions = valid_add(vector)
    else:
        actions = valid_substract(vector)

    for action in actions:
        new_vector = copy.deepcopy(vector)
        for i in range(3):
            if new_vector[2] == 0:
                new_vector[i] += action[i]
            else:
                new_vector[i] -= action[i]

        if sum(new_vector) == 0:
            if print_steps:
                print(moves, new_vector)
            solution = moves
            return True

        if solve(new_vector, moves, print_steps):
            if print_steps:
                print(moves, new_vector)
            return True

    return False

solve(start, 0, False)

print(solution)
