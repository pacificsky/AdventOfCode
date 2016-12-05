MIN_X = 0
MAX_X = 2
MIN_Y = 0
MAX_Y = 2

KEYPAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def isValidMove(position):
    x = position[0]
    y = position[1]
    if x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y:
        return False

    return True

def getDigit(position):
    return KEYPAD[position[0]][position[1]]

def main():
    f = open('day2_1_input.txt', 'r')
    lineCount = 0

    pos = [1,1] # starting position

    for line in f:
        lineCount += 1
        print "Processing line {0} with length {1}".format(lineCount, len(line))

        line = line.strip().rstrip('\n')

        print "Stripped length is {0}".format(len(line))

        for move in line:
            newpos = [pos[0], pos[1]]
            if move == 'U':
                newpos[0] -= 1
            elif move == 'D':
                newpos[0] += 1
            elif move == 'L':
                newpos[1] -= 1
            else:
                assert move == 'R'
                newpos[1] += 1

            if isValidMove(newpos):
                pos = newpos


        print getDigit(pos)

    print "All done!"
# run the script
main()