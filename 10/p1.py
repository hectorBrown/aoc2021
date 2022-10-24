PATH = "10/data.txt"

lines = [x[:-1] for x in open(PATH).readlines()]

map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
errormap = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

errors = []
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
                    errors.append(char)
                    errored = True
                
score = 0
for error in errors:
    score += errormap[error]

print(score)
