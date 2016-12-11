# http://adventofcode.com/2016/day/8
import parse

RECT = 1
ROTATE_ROW = 2
ROTATE_COL = 3

WIDTH_X = 50
HEIGHT_Y = 6


def init():
    screen_state = [None for y in range(HEIGHT_Y)]
    for y in range(HEIGHT_Y):
        screen_state[y] = [0 for x in range(WIDTH_X)]

    return screen_state


def get_instr(line):
    data = parse.parse("rect {}x{}", line)
    if data:
        return tuple([RECT, {"a": int(data[0]), "b": int(data[1])}])

    data = parse.parse("rotate row y={} by {}", line)
    if data:
        return tuple([ROTATE_ROW, {"y": int(data[0]), "b": int(data[1])}])

    data = parse.parse("rotate column x={} by {}", line)
    assert data is not None
    return tuple([ROTATE_COL, {"x": int(data[0]), "b": int(data[1])}])


def rect(size_x, size_y, screen_state):
    for y in range(size_y):
        for x in range(size_x):
            screen_state[y][x] = 1


def rotate_row(row_y, distance, screen_state):
    index = len(screen_state[row_y]) - distance
    screen_state[row_y] = screen_state[row_y][index:] + screen_state[row_y][:index]


def rotate_col(col_x, distance, screen_state):
    temp_row = [None]
    temp_row[0] = [0 for y in range(HEIGHT_Y)]
    for y in range(HEIGHT_Y):
        temp_row[0][y] = screen_state[y][col_x]

    rotate_row(0, distance, temp_row)

    for y in range(HEIGHT_Y):
        screen_state[y][col_x] = temp_row[0][y]


def process(instr, screen_state):
    opcode = instr[0]
    if opcode == RECT:
        rect(instr[1]["a"], instr[1]["b"], screen_state)
    elif opcode == ROTATE_ROW:
        rotate_row(instr[1]["y"], instr[1]["b"], screen_state)
    else:
        assert opcode == ROTATE_COL
        rotate_col(instr[1]["x"], instr[1]["b"], screen_state)


def count_lit_pixels(screen_state):
    count = 0
    for y in range(HEIGHT_Y):
        for x in range(WIDTH_X):
            if screen_state[y][x] == 1:
                count += 1

    return count


def display_board(screen_state):
    for y in range(len(screen_state)):
        string = ""
        for x in range(len(screen_state[y])):
            if x % 5 == 0:
                string = string + "  "

            if screen_state[y][x] == 0:
                string = string + " "
            else:
                assert screen_state[y][x] == 1
                string = string + "#"

        print string


def main():
    screen_state = init()
    print "Screen width: {0}".format(len(screen_state[0]))
    print "Screen height: {0}".format(len(screen_state))
    instruction_count = 0

    f = open("day8_1_input.txt", "r")
    for line in f:
        line = line.rstrip().rstrip("\n")
        instr = get_instr(line)
        process(instr, screen_state)
        instruction_count += 1
        #print "Lit pixels after instr {0}: {1}".format(instruction_count, count_lit_pixels(screen_state))

    print "Final lit pixels: {0}".format(count_lit_pixels(screen_state))
    display_board(screen_state)


main()