PATH = "day6/data.txt"

def propagate(state):
    new = []
    for fish in state:
        new += fish.propagate()
    state += new

class Lanternfish():
    def __init__(self, timer):
        self.__timer = timer
    
    def propagate(self):
        self.__timer -= 1
        if self.__timer < 0:
            self.__timer = 6
            return [Lanternfish(8)]
        else:
            return []

state = [Lanternfish(int(x)) for x in open(PATH).readline().split(",")]

for i in range(80):
    propagate(state)

print(len(state))
