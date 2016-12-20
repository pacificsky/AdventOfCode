# http://adventofcode.com/2016/day/19
import sys

DATA = 3017957
#DATA = 5

def main():

    elves = [1 for i in range(DATA)]
    print "Starting computation"

    x = 0
    index_found = -1
    iteration = 0
    remaining = DATA
    while True:
        if elves[x] == 0:
            x = (x + 1) % DATA
        else:
            i = (x + 1) % DATA
            while elves[i] == 0:
                i = (i + 1) % DATA
                if i == x:
                    print "Found!!! {0}".format(x + 1)
                    return

            elves[x] += elves[i]
            elves[i] = 0
            remaining -= 1

            x = (i + 1) % DATA

        if x == 0:
            iteration += 1
            print "Iteration {0}, remaining {1}".format(iteration, remaining)


    print index_found


main()