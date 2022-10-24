PATH = "14/data.txt"

def step(template):
    i = 1
    while i < len(template):
        pair = template[i - 1:i + 1]
        if pair in rules:
            template = template[:i] + rules[pair] + template[i:]
            i += 1
        i += 1
    return template


template, rules = "".join(open(PATH).readlines()).split("\n\n")
rules = {x.split(" -> ")[0]:x.split(" -> ")[1] for x in rules.split("\n")[:-1]}

elements = []

for rule in rules:
    references = [rule[0], rule[1], rules[rule]]
    for ref in references:
        if not ref in elements:
            elements.append(ref)

for i in range(10):
    template = step(template)

elem_counts = [template.count(x) for x in elements]

print(max(elem_counts) - min(elem_counts))
