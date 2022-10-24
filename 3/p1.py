import numpy as np
PATH = "3/data.txt"

def to_decimal(input):
    exponent = 1
    total = 0
    for digit in input[::-1]:
        total += exponent * int(digit)
        exponent *= 2
    return total

input = np.array([[int(y) for y in x[:-1]] for x in open(PATH).readlines()]).transpose()

gamma = [1 if list(x).count(1) > input.shape[1] / 2 else 0 for x in input]
eps = [abs(x - 1) for x in gamma]
print(to_decimal(eps) * to_decimal(gamma))
