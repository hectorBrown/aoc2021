import math
PATH = "17/data.txt"
def ext_tri(n):
    if n >= 0:
        return sum(range(n + 1))
    else:
        return sum(range(n, 0))

def get_vys(N, y_lim):
    _y_lim = [(x + sum(range(N))) / N for x in y_lim]
    _y_lim[0] = math.ceil(_y_lim[0])
    _y_lim[1] = math.floor(_y_lim[1])
    return list(range(_y_lim[0], _y_lim[1] + 1))
    
def get_max_steps(y_lim):
    return 2 * (max([abs(x) for x in y_lim]))

def get_vxs(N, x_lim):
    vxs = []
    #N > v_x
    for i in range(min(0, x_lim[0]), max(0, x_lim[1])):
        tri = ext_tri(i)
        if tri >= x_lim[0] and tri <= x_lim[1] and N > i:
            vxs.append(i)
    #N < v_x
    if x_lim[0] > 0:
        _x_lim = [(x + sum(range(N))) / N for x in x_lim]
        _x_lim[0] = math.ceil(_x_lim[0])
        _x_lim[1] = math.floor(_x_lim[1])
        vxs += filter(lambda x : x >= N, range(_x_lim[0], _x_lim[1] + 1))
    elif x_lim[0] < 0 and x_lim[1] > 0:
        _x_lim[1] = math.floor((x_lim[1] + sum(range(N)) / N))
        _x_lim[0] = math.ceil((x_lim[0] - sum(range(N)) / N))
        vxs += filter(lambda x : x >= N, range(_x_lim[0], _x_lim[1] + 1))
    else:
        _x_lim = [(x - sum(range(N))) / N for x in x_lim]
        _x_lim[0] = math.ceil(_x_lim[0])
        _x_lim[1] = math.floor(_x_lim[1])
        vxs += filter(lambda x : x >= N, range(_x_lim[0], _x_lim[1] + 1))
    return vxs
shape = [tuple([int(y) for y in x.split("=")[1][:-1].split("..")]) for x in open(PATH).readline().split(" ")[2:]]
vs = []
for i in range(1,get_max_steps(shape[1]) + 1):
    vs.append([get_vxs(i, shape[0]), get_vys(i, shape[1])])
tot = 0
modes = []
for mode in vs:
    for x in mode[0]:
        for y in mode[1]:
            if not [x, y] in modes:
                modes.append([x, y])
                tot += 1

print(tot)