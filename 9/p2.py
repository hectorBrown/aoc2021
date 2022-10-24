PATH = "9/data.txt"
def get_neighbours(point):
    neighbours = []
    for x_step in range(-1, 2):
        for y_step in range(-1, 2):
            x = point[0] + x_step
            y = point[1] + y_step
            if x >= 0 and x < len(map[0]):
                if y >= 0 and y < len(map):
                    if not (x_step == y_step or x_step == -y_step):
                        neighbours.append([x, y])
    return neighbours

def propagate_basin(point, basin):
    for nei in get_neighbours(point):
        if map[nei[1]][nei[0]][0] != 9 and map[nei[1]][nei[0]][1] is None:
            map[nei[1]][nei[0]][1] = basin
            propagate_basin(nei, basin)

def get_basin_size(basin):
    return sum([len(list(filter(lambda x : x[1] == basin, line))) for line in map])

map = [[[int(x),None] for x in line[:-1]] for line in open(PATH).readlines()]

basins = []
for y in range(len(map)):
    for x in range(len(map[0])):
        if all([map[y][x][0] < map[z[1]][z[0]][0] for z in get_neighbours([x, y])]):
            map[y][x][1] = (x, y)
            propagate_basin([x, y], (x, y))
            basins.append((x,y))

largest = sorted(basins, key=lambda x : get_basin_size(x))[-3:]
prod = 1
for basin in largest:
    prod *= get_basin_size(basin)
print(prod)
