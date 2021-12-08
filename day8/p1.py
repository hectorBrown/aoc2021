PATH = "day8/data.txt"

input = [x.split("|")[1].split(" ")[1:] for x in open(PATH).readlines()]
for line in input:
    line[-1] = line[-1][:-1]

count = 0
for line in input:
    for output in line:
        if len(output) in [2, 4, 3, 7]:
            count += 1 
        
print(count)
