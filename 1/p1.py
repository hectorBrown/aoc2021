PATH = "1/data.txt"
input = [int(x[:-1]) for x in open(PATH).readlines()]

count = 0
for i in range(1, len(input)):
    if input[i - 1] < input[i]:
        count += 1

print(count)
