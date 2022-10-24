PATH = "10/data.txt"

lines = [x[:-1] for x in open(PATH).readlines()]

map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
autocompletemap = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

incomplete = []
for line in lines:
    chunks = []
    errored = False
    for char in line:
        if not errored:
            if char in ["(", "[", "{", "<"]:
                chunks.append(char)
            else:
                if char == map[chunks[-1]]:
                    chunks.pop()
                else:
                    errored = True
    if not errored:
        incomplete.append(line)

completion_scores = []
for line in incomplete:
    chunks = []
    for char in line:
        if char in ["(", "[", "{", "<"]:
            chunks.append(char)
        else:
            chunks.pop()
    score = 0
    while len(chunks) > 0:
        score *= 5; score += autocompletemap[map[chunks.pop()]]
    completion_scores.append(score)

print(sorted(completion_scores)[int((len(completion_scores) - 1) / 2)])
