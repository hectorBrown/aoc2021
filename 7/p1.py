PATH = "7/data.txt"

def cost(crabs, target):
    return sum(map(lambda x : abs(x - target), crabs))

crabs = [int(x) for x in open(PATH).readline().split(",")]

target = 0; currcost = cost(crabs, 0)
for i in range(min(crabs), max(crabs)):
    if cost(crabs, i) < currcost:
        currcost = cost(crabs, i)
        target = i

print(cost(crabs, target))


