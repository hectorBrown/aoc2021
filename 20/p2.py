PATH = "20/data.txt"

class InfImg:

    def __init__(self, _dict, _lims, _uniform=0):
        self.lims = _lims
        self.dict = _dict
        self.uniform = _uniform
    
    @classmethod
    def from_raw(cls, raw):
        lims = [[0, len(raw)], [0, len(raw[0])]]
        dict = {row : {col : int(raw[row][col] == '#') for col in range(*lims[1])} for row in range(*lims[0])}
        return cls(dict, lims)

    def __str__(self):
        output = ""
        for row in range(*self.lims[0]):
            for col in range(*self.lims[1]):
                if bool(self.get_pixel(row, col)):
                    output += "#"
                else:
                    output += "."
            output += "\n"
        return output

    def get_pixel(self, row, col):
        if row in self.dict:
            if col in self.dict[row]:
                return self.dict[row][col]
        return self.uniform

    def enhance(self, alg):
        new_lims = [[self.lims[x][y] for y in range(0, 2)] for x in range(0, 2)]
        new_lims[0][0] -= 1; new_lims[1][0] -= 1
        new_lims[0][1] += 1; new_lims[1][1] += 1
        new = {}
        for row in range(*new_lims[0]):
            new[row] = {}
            for col in range(*new_lims[1]):
                key = ""
                for row_scan in range(-1, 2):
                    for col_scan in range(-1, 2):
                        key += str(self.get_pixel(row + row_scan, col + col_scan))
                new[row][col] = alg[int(key, 2)]
        new_uni = 0
        #if uni is 0 and alg[0] is 1 or if uni is 1 and alg[511] is 1
        if (self.uniform == 0 and alg[0] == 1) or (self.uniform == 1 and alg[511] == 1):
            new_uni = 1

        return InfImg(new, new_lims, _uniform=new_uni)
    
    def count(self):
        count = 0
        for row in range(*self.lims[0]):
            for col in range(*self.lims[1]):
                count += self.get_pixel(row, col)
        return count

alg, img_dat = open(PATH).read().split("\n\n")
alg = list(map(lambda x : 1 if x == '#' else 0, alg))
img = InfImg.from_raw(img_dat.split("\n")[:-1])

for i in range(50):
    done = (i / 50) * 100
    print("%d%% enhanced" % done)
    img = img.enhance(alg)

print(img)
print(img.count())