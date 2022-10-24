PATH = "15/data.txt"

def get_neighbours(x, y):
    neis = []
    for x_step in range(-1, 2):
        for y_step in range(-1, 2):
            nei_x = x + x_step; nei_y = y + y_step
            if (x_step == 0 or y_step == 0) and nei_x >= 0 and nei_y >= 0 and nei_x < len(risks[0]) and nei_y < len(risks) and not (x_step == 0 and y_step == 0):
                neis.append((nei_x, nei_y))
    return neis

risks = [[int(x) for x in line[:-1]] for line in open(PATH).readlines()]

active_paths = {(0,0): 0}
covered = []

while (len(risks[0]) - 1, len(risks) - 1) not in active_paths:
    min_pos = list(active_paths.keys())[0]
    min_path = active_paths[min_pos]
    for pos in active_paths:
        if active_paths[pos] < min_path:
            min_path = active_paths[pos]
            min_pos = pos
    neis = get_neighbours(*min_pos)
    for nei in neis:
        if not nei in covered and not nei in active_paths:
            active_paths[nei] = risks[nei[1]][nei[0]] + min_path
    covered.append(min_pos)
    active_paths.pop(min_pos)
print(active_paths[(len(risks[0]) - 1, len(risks) - 1)])
