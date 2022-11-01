import numpy as np
import pickle
ex_data = "data"
PATH = "19/" + ex_data + ".txt"


def safe_inv(mat):
    return round_mat(np.linalg.inv(mat))


def safe_mul(m1, m2):
    return round_mat(np.matmul(m1, m2))


def round_mat(mat):
    _mat = np.array(mat)
    for i, row in enumerate(_mat):
        for j, col in enumerate(row):
            _mat[i][j] = round(_mat[i][j])
    return np.matrix(_mat)


rot_yx = np.matrix([[0, -1, 0, 0],
                    [1, 0, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
rot_yz = np.matrix([[1, 0, 0, 0],
                    [0, 0, 1, 0],
                    [0, -1, 0, 0],
                    [0, 0, 0, 1]])
rot_zx = np.matrix([[0, 0, -1, 0],
                    [0, 1, 0, 0],
                    [1, 0, 0, 0],
                    [0, 0, 0, 1]])
id = np.matrix([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
rot_faces = [id, rot_yz, safe_mul(rot_yz, rot_yz), safe_mul(safe_mul(rot_yz, rot_yz), rot_yz),
             rot_zx, safe_mul(safe_mul(rot_zx, rot_zx), rot_zx)]
rots = []
for face in rot_faces:
    rots += [safe_mul(id, face),
             safe_mul(rot_yx, face),
             safe_mul(safe_mul(rot_yx, rot_yx), face),
             safe_mul(safe_mul(safe_mul(rot_yx, rot_yx), rot_yx), face)]


class Scanner:
    def __init__(self, _beacons, _id):
        self.beacons = np.array(_beacons)
        self.id = _id

    def __repr__(self):
        return "Scanner: {beacons: %s}" % self.beacons

    def get_transed(self, mat):
        return np.array(np.transpose(safe_mul(mat, np.transpose(self.beacons))))


class Group:
    def __init__(self, parent):
        self.children = [parent]
        self.transs = [id]
        self.parent = 0

    def __repr__(self):
        return "Group: {Scanners (%s)}" % str([x.id for x in self.children])

    def merge(self, group, mat):
        self.children += group.children
        self.transs += [safe_mul(mat, x) for x in group.transs]

    def reparent(self, c_i):
        self.transs = [safe_mul(safe_inv(self.transs[c_i]), x)
                       for x in self.transs]
        self.parent = c_i

    def get_beacons(self):
        beacons = []
        for i, child in enumerate(self.children):
            c_beacons = child.get_transed(self.transs[i])
            beacons += list(filter(lambda x: not any(
                [all([x[i] == y[i] for i in range(len(x))]) for y in beacons]), c_beacons))
        return beacons
    
    def get_dist(self, c_i_a, c_i_b):
        _parent = self.parent
        self.reparent(c_i_a)
        ans = sum([abs(x) for x in np.transpose(self.transs[c_i_b])[-1].tolist()[0][:-1]])
        self.reparent(_parent)
        return int(ans)


def get_trans_mat(x, y, z):
    return np.matrix([[1, 0, 0, x],
                      [0, 1, 0, y],
                      [0, 0, 1, z],
                      [0, 0, 0, 1]])


def match(sca, scb):
    #can still speed this up by generating rotation from points (iterate over n - 12)
    for origin_a in sca.beacons[:-12]:
        for origin_b in scb.beacons:
            transl_a = get_trans_mat(*[-x for x in origin_a[:-1]])
            transl_b = get_trans_mat(*[-x for x in origin_b[:-1]])
            trace_a = [sum([abs(y) for y in x])
                       for x in sca.get_transed(transl_a)]
            trace_b = [sum([abs(y) for y in x])
                       for x in scb.get_transed(transl_b)]
            if len(list(filter(lambda x: x in trace_b, trace_a))) >= 12:
                for rot in rots:
                    trans = safe_mul(rot, transl_a)
                    sca_trans = sca.get_transed(trans)
                    scb_trans = scb.get_transed(transl_b)
                    common = 0
                    for beacon_a in sca_trans:
                        for beacon_b in scb_trans:
                            if all([beacon_a[i] == beacon_b[i] for i in range(len(beacon_a))]):
                                common += 1
                    if common >= 12:
                        return safe_inv(safe_mul(safe_inv(transl_b), trans))
    return None


def perform_merge(groups):
    #can speed this up by only blocking merging with the same scanner... groups can simultaneously merge with multiple others
    merge_groups = []
    merge_trans = []
    for group_a in groups:
        for group_b in groups:
            if group_a != group_b and group_a not in [x for pair in merge_groups for x in pair] and group_b not in [x for pair in merge_groups for x in pair]:
                merged = False
                for c_i_a, sca in enumerate(group_a.children):
                    for c_i_b, scb in enumerate(group_b.children):
                        if not merged:
                            _match = match(sca, scb)
                            if not _match is None:
                                merged = True
                                group_a.reparent(c_i_a)
                                group_b.reparent(c_i_b)
                                merge_groups.append((group_a, group_b))
                                merge_trans.append(_match)
                                print("Found match between %s, %s" %
                                      (sca.id, scb.id))
    return (merge_groups, merge_trans)


scanners = [Scanner([[int(z) for z in y.split(",")] + [1] for y in x.split("\n")[1:]], i)
            for i, x in enumerate(open(PATH).read().split("\n\n"))]
groups = [Group(scanner) for scanner in scanners]

while len(groups) > 1:
    merge_groups, merge_trans = perform_merge(groups)
    for i, pair in enumerate(merge_groups):
        print("Merging %s, %s" % (pair[0], pair[1]))
        pair[0].merge(pair[1], merge_trans[i])
        groups.remove(pair[1])
    print("Current groups %s" % str(groups))
print("Map complete")
with open("19/" + ex_data + ".pkl", "wb") as f:
    pickle.dump(groups, f)

#with open("19/" + ex_data + ".pkl", "rb") as f:
#   groups = pickle.load(f)

dists = []
for c_i_a in range(len(groups[0].children)):
    for c_i_b in range(len(groups[0].children)):
        if c_i_a != c_i_b:
            dists.append(groups[0].get_dist(c_i_a, c_i_b))
print(max(dists))