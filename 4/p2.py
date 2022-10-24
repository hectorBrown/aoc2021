PATH = "4/data.txt"

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
        boards.append([board, False])
        board = []
    else:
        board.append([[int(x), False] for x in line.replace("  ", " ").strip().split(" ")])

won = 0; i = 0; score = 0

while won != len(boards):
    number = numbers[i]
    for board in boards:
        for row in board[0]:
            for square in row:
                if square[0] == number:
                    square[1] = True
    for board in boards:
        if not board[1]:
            for row in board[0]:
                if all([x[1] for x in row]):
                    won += 1
                    board[1] = True
                    score = get_score(board[0]) * number
            for col in transpose(board[0]):
                if all([x[1] for x in col]) and not board[1]:
                    won += 1
                    board[1] = True
                    score = get_score(board[0]) * number

    i += 1
print(score)
