PATH = "day9/data.txt"

map = [[int(x) for x in line[:-1]] for line in open(PATH).readlines()]

risk = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        pt = map[y][x]
        lowest = True
        for x_step in range(-1,2):
            for y_step in range(-1, 2):
                x_check = x + x_step; y_check = y + y_step
                if x_check >= 0 and x_check < len(map[0]) and y_check >= 0 and y_check < len(map):
                    if not(x_check == x and y_check == y):
                        if map[y_check][x_check] <= pt:
                            lowest = False
        if lowest:
            risk += pt + 1

print(risk)
