"""
In this project I going to write the solution for a nonogram problem. This exercice is from DataWars.
This is the problem: given a binary array (a list containing only 1s and 0s), return a list of positive integers that represent the lengths of the sets of consecutive 1's in the input array, in order from left to right.

Example:

    [1, 1, 1, 0, 1, 1] => [3, 2]
    [1, 0, 1, 1, 1, 1] => [1, 4]
    [1, 1, 1, 1, 1, 1] => [6]
    [1, 0, 1, 0, 1, 1] => [1, 1, 2]
    [0, 0, 0, 0, 0, 0] => []
"""

def nonogram_sequence(array):
    counter = 0
    sequence = []
    for item in array:
        if item == 1:
            counter += 1
        else:
            sequence.append(counter)
            counter = 0
    if counter:
        sequence.append(counter)
        return sequence
print(nonogram_sequence([1, 1, 1, 0, 1, 1]))
