import numpy as np
PATH = "3/data.txt"

def to_decimal(input):
    exponent = 1
    total = 0
    for digit in input[::-1]:
        total += exponent * int(digit)
        exponent *= 2
    return total

input = np.array([[int(y) for y in x[:-1]] for x in open(PATH).readlines()])


ogr_list = np.array([x.copy() for x in input])
bit = 0
while len(ogr_list) > 1:
    next_list = []
    remove = []
    gamma = [1 if list(x).count(1) >= ogr_list.transpose().shape[1] / 2 else 0 for x in ogr_list.transpose()]
    for i, number in enumerate(ogr_list):
        if number[bit] == gamma[bit]:
            next_list.append(number)
    ogr_list = np.array(next_list)
    bit += 1

ogr = ogr_list[0]

csr_list = np.array([x.copy() for x in input])
bit = 0

while len(csr_list) > 1:
    next_list = []
    remove = []
    eps = [0 if list(x).count(1) >= csr_list.transpose().shape[1] / 2 else 1 for x in csr_list.transpose()]
    for i, number in enumerate(csr_list):
        if number[bit] == eps[bit]:
            next_list.append(number)
    csr_list = np.array(next_list)
    bit += 1

csr = csr_list[0]

print(to_decimal(ogr) * to_decimal(csr))