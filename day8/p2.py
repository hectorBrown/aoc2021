PATH = "day8/data.txt"

def list_to_string(list):
    output = ""
    for char in list:
        output += char
    return output

def get_switchboard(uniques):
    cf = list(filter(lambda x : len(x) == 2, uniques))[0]
    acf = list(filter(lambda x : len(x) == 3, uniques))[0]
    a = list(filter(lambda x : x not in cf, acf))[0]
    bcdf = list(filter(lambda x : len(x) == 4, uniques))[0]
    bd = bcdf.replace(cf[0], "").replace(cf[1], "")
    abcdf = a + bcdf
    abcdfg = list(filter(lambda x : [y in abcdf for y in x].count(True) == 5 and len(x) == 6, uniques))[0]
    g = list(filter(lambda x : x not in abcdf, abcdfg))[0]
    acfg = a + cf + g
    acdfg = list(filter(lambda x : [y in acfg for y in x].count(True) == 4 and len(x) == 5, uniques))[0]
    d = list(filter(lambda x : x not in acfg, acdfg))[0]
    b = list(filter(lambda x : x != d, bd))[0]
    abdg = a + bd + g
    abdfg = list(filter(lambda x : [y in abdg for y in x].count(True) == 4 and len(x) == 5, uniques))[0]
    f = list(filter(lambda x : x not in abdg, abdfg))[0]
    c = list(filter(lambda x : x != f, cf))[0]
    e = list(filter(lambda x : x not in abcdfg, "abcdefg"))[0]
    switch = [
        ("a", a),
        ("b", b),
        ("c", c),
        ("d", d),
        ("e", e),
        ("f", f),
        ("g", g)
    ]
    return switch

map = [
    (0, "abcefg"),
    (1, "cf"),
    (2, "acdeg"),
    (3, "acdfg"),
    (4, "bcdf"),
    (5, "abdfg"),
    (6, "abdefg"),
    (7, "acf"),
    (8, "abcdefg"),
    (9, "abcdfg")
]

input = [[y.split(" ") for y in x.split("|")] for x in open(PATH).readlines()]

for line in input:
    line[0] = line[0][:-1]
    line[1] = line[1][1:]
    line[1][-1] = line[1][-1][:-1]

values = []
for line in input:
    switch = get_switchboard(line[0])
    value = ""
    for output in line[1]:
        lookup = {x[1]: x[0] for x in switch}
        decoded = [lookup[x] for x in output]
        map_lookup = {x[1]: x[0] for x in map}
        value += str(map_lookup[list_to_string(sorted(decoded))])
    values.append(int(value))

print(sum(values))
        