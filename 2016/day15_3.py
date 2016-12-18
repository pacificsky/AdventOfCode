# http://adventofcode.com/2016/day/15
# https://www.reddit.com/r/adventofcode/comments/5ifvyc/2016_day_15_part_3_our_discs_got_larger/
import sys

class Disc:
    def __init__(self, index, positions, current):
        self.index = index
        self.positions = positions
        self.current = current

    def __str__(self):
        return "Disc:{0}, Positions:{1}, Current:{2}".format(self.index, self.positions, self.current)


def main():
    discs = [Disc(1, 43, 42), Disc(2, 53, 47), Disc(3, 61, 50), Disc(4, 37, 5), Disc(5, 127, 49)]

    index = 40

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
                disc.current = (disc.current + 43) % disc.positions

        index += 43

        sys.stdout.write("Index: {0}\r".format(index))

    print "Found a match at time {0}".format(index)
    for disc in discs:
        print disc




main()
