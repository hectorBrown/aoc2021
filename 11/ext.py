import matplotlib.pyplot as plt, matplotlib.animation as anim, numpy as np, random

PATH = "11/data.txt"

def print_map():
    output = ""
    for row in map:
        for oct in row:
            output += str(oct)
        output += "\n"
    print(output)

def get_neighbours(pos):
    neis = []
    for x_step in range(-1, 2):
        for y_step in range(-1, 2):
            x = pos[0] + x_step; y = pos[1] + y_step
            if not (x_step == 0 and y_step == 0) and x >= 0 and y >= 0 and x < len(map[0]) and y < len(map):
                neis.append((x, y))
    return neis

def step():
    for row in map:
        for i in range(len(row)):
            row[i] += 1
    
    flashed = []
    was_flash = True
    while was_flash:
        was_flash = False
        for y, row in enumerate(map):
            for x in range(len(row)):
                if row[x] > 9 and [x, y] not in flashed:
                    was_flash = True
                    flashed.append([x,y])
                    for nei in get_neighbours((x, y)):
                        map[nei[1]][nei[0]] += 1
    
    for oct in flashed:
        map[oct[1]][oct[0]] = 0                

    image = np.array([[[(map[y][x] / 9), (map[y][x] / 9), (map[y][x] / 9)] for y in range(len(map))] for x in range(len(map[0]))])
    return [plt.imshow(image)]
    
    
                
#map = [list(map(lambda x : int(x), y[:-1])) for y in open(PATH).readlines()]

map = [[random.randint(0,9) for x in range(50)] for y in range(50)]

fig = plt.figure()
frames = []
for i in range(100):
    print(str(i / 100 * 100) + "%")
    frames.append(step())

ani = anim.ArtistAnimation(fig, frames, interval=50, blit=True, repeat_delay=1000)

plt.show()
