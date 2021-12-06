PATH = "day6/data.txt"

def new(state):
    new = {}
    for timer in state:
        if timer != 0:
            if timer - 1 in new.keys():
                new[timer - 1] += state[timer]
            else:
                new[timer - 1] = state[timer]
        else:
            if 6 in new.keys():
                new[6] += state[timer]
            else:
                new[6] = state[timer]
            if 8 in new.keys():
                new[8] += state[timer]
            else:
                new[8] = state[timer]
    return new


input = [int(x) for x in open(PATH).readline().split(",")]

state = {}

for fish in input:
    if not fish in state.keys():
        state[fish] = 1
    else:
        state[fish] += 1


for i in range(256):
    state = new(state)

print(sum([state[x] for x in state]))
