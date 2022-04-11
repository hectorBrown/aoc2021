PATH = "day4/data.txt"

def get_score(board):
    sum = 0
    for row in board:
        for square in row:
            if not square[1]:
                sum += square[0]
    return sum

def transpose(list):
    transposed = []
    for col_i in range(len(list[0])):
        col = []
        for row_i in range(len(list)): 
            col.append(list[row_i][col_i])
        transposed.append(col)
    return transposed

raw = open(PATH).readlines()
raw.append("\n")
numbers = [int(x) for x in raw[0].split(",")]

boards = []
board = []
for line in raw[2:]:
    if line == "\n":
        boards.append(board)
        board = []
    else:
        board.append([[int(x), False] for x in line.replace("  ", " ").strip().split(" ")])

won = False; i = 0; score = 0

while not won:
    number = numbers[i]
    for board in boards:
        for row in board:
            for square in row:
                if square[0] == number:
                    square[1] = True
    for board in boards:
        for row in board:
            if all([x[1] for x in row]):
                won = True
                score = get_score(board) * number
        for col in transpose(board):
            if all([x[1] for x in col]):
                won = True
                score = get_score(board) * number

    i += 1
print(score)
