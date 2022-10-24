PATH = "14/data.txt"
def step(pairs):
    new_first = ""; new_last = ""
    global first; global last;
    new_pairs = {}
    for pair in pairs:
        new_1 = pair[0] + rules[pair]
        new_2 = rules[pair] + pair[1]
        if pair == first:
            new_first = new_1
        if pair == last:
            new_last = new_2
        if new_1 in new_pairs:
            new_pairs[new_1] += pairs[pair]
        else:
            new_pairs[new_1] = pairs[pair]
        if new_2 in new_pairs:
            new_pairs[new_2] += pairs[pair]
        else:
            new_pairs[new_2] = pairs[pair]
    first = new_first; last = new_last;
    return new_pairs


template, rules = "".join(open(PATH).readlines()).split("\n\n")
rules = {x.split(" -> ")[0]:x.split(" -> ")[1] for x in rules.split("\n")[:-1]}

elements = []

for rule in rules:
    references = [rule[0], rule[1], rules[rule]]
    for ref in references:
        if not ref in elements:
            elements.append(ref)

pairs = {}
first = template[:2]; last = template[-2:]
for i in range(1, len(template)):
    pair = template[i - 1:i + 1]
    if not pair in pairs:
        pairs[pair] = 1
    else:
        pairs[pair] += 1

for i in range(40):
    pairs = step(pairs)

elem_counts = []
for elem in elements:
    count = 0
    for pair in pairs:
        count += pair.count(elem) * pairs[pair]
    count /= 2
    if elem == first[0] or elem == last[1]:
        count += 0.5
    elem_counts.append(int(count))

print(max(elem_counts) - min(elem_counts))
