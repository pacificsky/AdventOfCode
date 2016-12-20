# http://adventofcode.com/2016/day/19
import sys

DATA = 3017957
#DATA = 5

PRINT_DEBUG = False


def DEBUG(string):
    if PRINT_DEBUG:
        print string


# direction is +1 for move forward, -1 for move backward
def move_target_index_by_offset(elves, target_index, offset, direction):
    assert direction in [1, -1]
    assert offset > 0
    length = len(elves)
    while offset > 0:
        target_index = (target_index + direction) % length
        while elves[target_index] is None:
            target_index = (target_index + direction) % length

        offset -= 1

    return target_index


def main2():
    elves = [(i + 1, 1) for i in range(DATA)]
    print "Starting computation"

    difference = 0
    cur_index = 0
    target_index = 0
    remaining = DATA
    number_elves = DATA
    
    iteration = 1

    while True:

        # Compute the new difference
        new_difference = 1 + (remaining - 2) / 2

        DEBUG("Old difference {0} New difference {1}".format(difference, new_difference))

        # Determine if the current difference matches the new difference
        # Adjust target if necessary
        if difference != new_difference:
            if difference < new_difference:
                target_index = move_target_index_by_offset(elves, target_index, new_difference - difference, 1)
                difference = new_difference
            else:
                assert difference > new_difference
                target_index = move_target_index_by_offset(elves, target_index, difference - new_difference, -1)
                difference = new_difference
                print "Target moved backwards!"

        assert difference == new_difference

        DEBUG("Remaining {0} difference {1}".format(remaining, difference))
        DEBUG("Elf {0} stealing from elf {1}".format(elves[cur_index][0], elves[target_index][0]))


        # Steal the presents
        elves[cur_index] = (elves[cur_index][0], elves[cur_index][1] + elves[target_index][1])
        elves[target_index] = None

        # Move target_index to point to the next elf with a present
        while elves[target_index] is None:
            target_index = (target_index + 1) % number_elves

        # Move cur_index forward by one
        cur_index = (cur_index + 1) % number_elves
        while elves[cur_index] is None:
            cur_index = (cur_index + 1) % number_elves

        # Update difference if necessary
        difference -= 1
        remaining -= 1

        DEBUG("- New cur_index {0} new target_index {1}".format(cur_index, target_index))
        DEBUG("- New current {0} new target {1}".format(elves[cur_index][0], elves[target_index][0]))


        # Are we done?
        if remaining == 1:
            print "Done!"
            print "Winner is {0}".format(elves[cur_index][0])
            break

        # After a full loop, compact
        if cur_index == 0:
            elves = filter(lambda item: item is not None, elves)
            number_elves = len(elves)
            target_index = 0
            difference = 0
            print "Iteration {0} done. Remaining {1}".format(iteration, remaining)
            iteration += 1




def main():

    elves = [(i, 1) for i in range(DATA)]
    print "Starting computation"

    remaining = DATA
    x = 0
    target = -1
    while remaining != 1:

        difference = (remaining - 2) / 2

        c = (x + difference + 1) % len(elves)

        new_val = elves[x][1] + elves[c][1]
        elves[x] = (elves[x][0], new_val)

        # if c == (len(elves) - 1):
        #     elves = elves[:c]
        # else:
        #     elves = elves[:c] + elves[c+1:]


        elves.remove(elves[c])


        remaining -= 1

        if c < x:
            x -= 1

        if remaining > 1:
            x = (x + 1) % len(elves)

        sys.stderr.write("Remaining: {0}\r".format(remaining))

    print "The last x is {0}".format(elves[x][0] + 1)


main2()