#SLOW
PATH = "day15/data.txt"

def get_neighbours(x, y):
    neis = []
    for x_step in range(-1, 2):
        for y_step in range(-1, 2):
            nei_x = x + x_step; nei_y = y + y_step
            if (x_step == 0 or y_step == 0) and nei_x >= 0 and nei_y >= 0 and nei_x < len(risks[0]) and nei_y < len(risks) and not (x_step == 0 and y_step == 0):
                neis.append((nei_x, nei_y))
    return neis

def shift(risks, n):
    new = [x.copy() for x in risks]
    for row in new:
        for i in range(len(row)):
            row[i] += n
            if row[i] > 9:
                row[i] -= 9
    return new

risks = [[int(x) for x in line[:-1]] for line in open(PATH).readlines()]

parent = [[shift(risks, x + y) for x in range(5)] for y in range(5)]

risks = []
for parent_y in range(len(parent)):
    for y in range(len(parent[0][0])):
        row = []
        for parent_x in range(len(parent[0])):
            for x in range(len(parent[0][0][0])):
                row.append(parent[parent_y][parent_x][y][x]) 
        risks.append(row)

active_paths = {(0,0): 0}
covered = []

while (len(risks[0]) - 1, len(risks) - 1) not in active_paths:
    min_path = active_paths[list(active_paths.keys())[0]]
    for pos in active_paths:
        if active_paths[pos] < min_path:
            min_path = active_paths[pos]
    min_poss = []
    for pos in active_paths:
        if active_paths[pos] == min_path:
            min_poss.append(pos)
    for min_pos in min_poss:
        neis = get_neighbours(*min_pos)
        for nei in neis:
            if not nei in covered and not nei in active_paths:
                active_paths[nei] = risks[nei[1]][nei[0]] + min_path
        covered.append(min_pos)
        active_paths.pop(min_pos)
print(active_paths[(len(risks[0]) - 1, len(risks) - 1)])
