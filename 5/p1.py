PATH = "day5/data.txt"

input = [[list(map(lambda x : int(x), y.split(","))) for y in x.split("->")] for x in open(PATH).readlines()]

map = []
max_x = max([max([x[0][0] for x in input]), max([x[1][0] for x in input])])
max_y = max([max([x[0][1] for x in input]), max([x[1][1] for x in input])])
for row in range(max_y + 1):
    map.append([])
    for col in range(max_x + 1):
        map[row].append(0)


for segment in input:
    p1 = segment[0]; p2 = segment[1]
    if p1[0] == p2[0]:
        x = p1[0]
        for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            map[y][x] += 1
    elif p1[1] == p2[1]:
        y = p1[1]
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            map[y][x] += 1

count = 0
for row in map:
    for pos in row:
        if pos >= 2:
            count += 1

print(count)
