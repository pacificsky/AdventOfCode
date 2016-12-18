# http://adventofcode.com/2016/day/17
import Queue
import hashlib

GRID_WIDTH = 4
GRID_HEIGHT = 4
PASSCODE = "mmsxrhfx"
TARGET = (3,3)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
DIRECTIONS_STR = ['U', 'D', 'L', 'R']

class Room:
    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.path = path


def run(queue):

    while queue.qsize() > 0:
        room = queue.get()

        print "Evaluating room ({0}, {1}) with path {2}".format(room.x, room.y, room.path)

        if (room.x, room.y) == TARGET:
            return room

        passcode = PASSCODE
        for x in room.path:
            passcode += x

        print "Passcode is {0}".format(passcode)

        hasher = hashlib.md5()
        hasher.update(passcode)
        hash = hasher.hexdigest().lower()

        door_state = hash[:4]
        print "Door state is {0}".format(door_state)

        for direction in DIRECTIONS:
            x = room.x + direction[0]
            y = room.y + direction[1]

            if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
                print "Door ({0}, {1}) is outside bounds".format(x, y)
                continue

            index = DIRECTIONS.index(direction)
            door_open = door_state[index] in ['b', 'c', 'd', 'e', 'f']

            if door_open:
                queue.put(Room(x, y, room.path + [DIRECTIONS_STR[index]]))
                print "Door ({0}, {1}) is open because of door state {2}".format(x, y, door_state[index])
            else:
                print "Door ({0}, {1}) is closed because of door state {2}".format(x, y, door_state[index])




def main():

    queue = Queue.Queue()
    queue.put(Room(0, 0, []))

    target_room = run(queue)

    if target_room:
        target_path = ""
        for x in target_room.path:
            target_path += x

        print target_path

    else:
        print "No path possible"


main()