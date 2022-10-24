PATH = "16/data.txt"

class Packet:
    def __init__(self, transmission):
        self.v = dec(transmission[:3])
        self.t = dec(transmission[3:6])
        if self.t == 4:
            self.val = None
            i = 6
            val_string = ""
            while i < len(transmission) and self.val is None:
                val_string += transmission[i + 1:i + 5]
                if transmission[i] == "0":
                    self.val = dec(val_string)
                    self.length = i + 5
                i += 5
        else:
            self.sub = []
            if transmission[6] == "0":
                sub_length = dec(transmission[7:22])
                self.length = sub_length + 22
                i = 22
                while i < 22 + sub_length:
                    self.sub.append(Packet(transmission[i:]))
                    i += self.sub[-1].length
            else:
                no_sub = dec(transmission[7:18])
                i = 18
                for j in range(no_sub):
                    self.sub.append(Packet(transmission[i:]))
                    i += self.sub[-1].length
                self.length = sum([x.length for x in self.sub]) + 18

def v_sum(packet):
    if packet.t == 4:
        return packet.v
    else:
        return packet.v + sum([v_sum(x) for x in packet.sub])
    
def dec(bin):
    output = 0
    exponent = 1
    for char in reversed(bin):
        output += exponent * int(char)
        exponent *= 2
    return output

hex_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}
input = open(PATH).readline()[:-1]

transmission = ""
for char in input:
    transmission += hex_map[char]

parent = Packet(transmission)

print(v_sum(parent))
