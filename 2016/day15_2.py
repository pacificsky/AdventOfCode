# http://adventofcode.com/2016/day/15

class Disc:
    def __init__(self, index, positions, current):
        self.index = index
        self.positions = positions
        self.current = current

    def __str__(self):
        return "Disc:{0}, Positions:{1}, Current:{2}".format(self.index, self.positions, self.current)


def main():
    discs = [Disc(1, 7, 0), Disc(2, 13, 0), Disc(3, 3, 2), Disc(4, 5, 2), Disc(5, 17, 0), Disc(6, 19, 7), Disc(7, 11, 0)]

    index = 0

    while True:
        matched = 0
        for disc in discs:
            if disc.current == (disc.positions - disc.index):
                matched += 1

        if matched == len(discs):
            break
        else:
            matched = 0
            for disc in discs:
                disc.current = (disc.current + 1) % disc.positions

        index += 1

    print "Found a match at time {0}".format(index)
    for disc in discs:
        print disc




main()
