# http://adventofcode.com/2016/day/13
import Queue
import sys


class Point:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x*100 + self.y


FAVORITE_NUMBER = 1362
#FAVORITE_NUMBER = 10
TARGET = Point(31, 39, 0)
#TARGET = Point(7, 4, 0)


def compute(x, y):
    return x*x + 3*x + 2*x*y + y + y*y + FAVORITE_NUMBER


def count_one_bits(number):
    count = 0
    while number > 0:
        count += (number & 1)
        number >>= 1

    return count


def is_wall(point):
    number = compute(point.x, point.y)
    one_bits = count_one_bits(number)
    return (one_bits % 2) == 1


def get_neighbors(point):
    nbrs = [Point(point.x + 1, point.y, 0), Point(point.x, point.y + 1, 0), None, None]
    if point.x > 0:
        nbrs[2] = Point(point.x - 1, point.y, 0)
    if point.y > 0:
        nbrs[3] = Point(point.x, point.y - 1, 0)

    return nbrs


def main():

    queue = Queue.Queue()
    seen = set([Point(1, 1, 0)])
    data = [["X" for y in range(51)] for x in range(51)]


    queue.put(Point(1, 1, 0))

    loop_count = 0
    part_2_count = 0

    while queue.qsize() > 0:
        point = queue.get()
        if point.distance > 50:
            print ""
            print "Total points covered: {0}".format(part_2_count)
            break

        part_2_count += 1
        loop_count += 1
        sys.stdout.write("Iteration: {0}, Loop count: {1}\r".format(point.distance, loop_count))
        sys.stdout.flush()

        data[point.x][point.y] = "o"

        # if point == TARGET:
        #     data[point.x][point.y] = "$"
        #     print ""
        #     print "Found Target at distance {0}".format(point.distance)
        #     break

        neighbors = get_neighbors(point)
        for neighbor in neighbors:
            if not neighbor:
                continue

            if neighbor in seen:
                continue

            seen.add(neighbor)

            if is_wall(neighbor):
                data[neighbor.x][neighbor.y] = "#"
            else:
                neighbor.distance = point.distance + 1
                queue.put(neighbor)


    # for x in range(len(data)):
    #     for y in range(len(data[x])):
    #         sys.stdout.write(data[x][y])
    #     print""



main()







