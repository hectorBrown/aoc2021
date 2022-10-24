PATH = "12/data.txt"

def is_big(cave):
    return ord(cave[0]) < 97 

def get_paths(cave, been=[]):
    paths = []
    if cave != "start" and not is_big(cave):
        been.append(cave)
    for route in caves[cave]:
        if not route in been + ["start"]:
            if route == "end":
                paths.append([cave, "end"])
            else:
                for path in get_paths(route, been=been.copy()):
                    paths.append([cave] + path)
    return paths


connections = [x[:-1].split("-") for x in open(PATH).readlines()]
caves = {}

for cx in connections:
    if not cx[0] in caves.keys():
        caves[cx[0]] = []
    if not cx[1] in caves.keys():
        caves[cx[1]] = []
    
    caves[cx[0]].append(cx[1])
    caves[cx[1]].append(cx[0])

paths = get_paths("start")

print(len(paths))
