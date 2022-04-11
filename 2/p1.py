PATH = "day2/data.txt"
input = [tuple(x.split(' ')) for x in open(PATH).readlines()]
input = [(x[0], int(x[1][:-1])) for x in input]

position = [0, 0]

for line in input:
    if line[0] == "forward":
        position[0] += line[1]
    elif line[0] == "down":
        position[1] += line[1]
    elif line[0] == "up":
        position[1] -= line[1]

print(position[0] * position[1])
