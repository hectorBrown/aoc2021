PATH = "day13/data.txt"

def print_paper():
    output = ""
    for row in paper:
        for dot in row:
            if dot:
                output += "#"
            else:
                output += "."
        output += "\n"
    print(output)

dots, folds = "".join(open(PATH).readlines()).split("\n\n")

dots = dots.split("\n"); folds = folds[:-1].split("\n")
dots = [list(map(lambda x : int(x), x.split(","))) for x in dots]
folds = [[x.split("=")[0][-1], int(x.split("=")[1])] for x in folds]

max_x = max([x[0] for x in dots]); max_y = max([x[1] for x in dots])
paper = []
for y in range(max_y + 1):
    paper.append([False] * (max_x + 1))

for dot in dots:
    paper[dot[1]][dot[0]] = True

fold = folds[0]
if fold[0] == "y":
    above = paper[:fold[1]]
    below = paper[fold[1]:]
    below = below[::-1]
    for y in range(len(above)):
        for x in range(len(above[0])):
            above[y][x] = above[y][x] or below[y][x]
    paper = above.copy()
else:
    left = [x[:fold[1]] for x in paper]
    right = [x[fold[1]:] for x in paper]
    right = [x[::-1] for x in right]
    for y in range(len(left)):
        for x in range(len(left[0])):
            left[y][x] = left[y][x] or right[y][x]
    paper = left.copy()

count = 0
for row in paper:
    for dot in row:
        if dot:
            count += 1
print(count)
