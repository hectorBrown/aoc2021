PATH = "1/data.txt"
input = [int(x[:-1]) for x in open(PATH).readlines()]

count = 0
for i in range(1, len(input) - 2):
    if sum(input[i-1:i+2]) < sum(input[i:i+3]):
        count += 1

print(count)
