import math
PATH = "18/data.txt"

def to_sn(input):
    return bin_map(parse(input))

def parse(input):
    if '[' not in input:
        return int(input)
    else:
        items = []
        nest = 0
        for scan in range(len(input)):
            if input[scan] == '[':
                nest += 1
            elif input[scan] == ']':
                nest -= 1
            elif input[scan] == ',' and nest == 1:
                items += [parse(input[1:scan]), parse(input[scan + 1:-1])]
        return items

def bin_map(raw, prefix=""):
    map = {}
    if type(raw) is int:
        map[prefix] = raw
    else:
        map |= bin_map(raw[0], prefix=prefix + "0")
        map |= bin_map(raw[1], prefix=prefix + "1")
    return map

def get_children(sn):
    filter_0 = list(filter(lambda x : x[0] == '0', sn))
    filter_1 = list(filter(lambda x : x[0] == '1', sn))
    if len(filter_0) > 1:
        ans_0 = {x[1:]:sn[x] for x in filter_0}
    else:
        ans_0 = sn[filter_0[0]]
    if len(filter_1) > 1:
        ans_1 = {x[1:]:sn[x] for x in filter_1}
    else:
        ans_1 = sn[filter_1[0]]
    return [ans_0, ans_1]

def mag(sn):
    if type(sn) is int:
        return sn
    else:
        children = get_children(sn)
        return 3 * mag(children[0]) + 2 * mag(children[1])

def add(sn1, sn2):
    return {"0" + x : sn1[x] for x in sn1} | {"1" + x : sn2[x] for x in sn2}

def explode(sn):
    _sn = sn.copy()
    deep = list(filter(lambda x: len(x) >= 5, _sn))
    if len(deep) == 0:
        return None
    pairs = []

    for pos in deep:
        if pos[-1] == "0" and pos[:-1] + "1" in deep:
            pairs.append(pos[:-1])

    expl = sort(pairs)[0]

    ord_keys = sort(_sn.keys())
    left = ord_keys.index(expl + "0")
    if left > 0:
        _sn[ord_keys[left - 1]] += _sn[expl + "0"]
    if left < len(ord_keys) - 2:
        _sn[ord_keys[left + 2]] += _sn[expl + "1"]
    _sn[expl] = 0
    _sn.pop(expl + "0"); _sn.pop(expl + "1")
    return _sn

def split(sn):
    _sn = sn.copy()
    large = list(filter(lambda x : _sn[x] >= 10, _sn))
    if len(large) == 0:
        return None
    
    splt = sort(large)[0]

    _sn[splt + "0"] = math.floor(_sn[splt] / 2)
    _sn[splt + "1"] = math.ceil(_sn[splt] / 2)
    _sn.pop(splt)
    return _sn

def sort(keys):
    if len(keys) <= 1:
        return keys
    else:
        keys_0 = ["0" + x for x in sort([x[1:] for x in list(filter(lambda x : x[0] == '0', keys))])]
        keys_1 = ["1" + x for x in sort([x[1:] for x in list(filter(lambda x : x[0] == '1', keys))])]
        return keys_0 + keys_1

def reduce(sn):
    _sn = sn.copy()
    action = True
    while action:
        action = False
        res = explode(_sn)
        if not res is None:
            _sn = res
            action = True
        else:
            res = split(_sn)
            if not res is None:
                _sn = res
                action = True
    return _sn

nums = [to_sn(x[:-1]) for x in open(PATH).readlines()]
tot = nums[0]
for i in range(1, len(nums)):
    tot = reduce(add(tot, nums[i]))
print(mag(tot))