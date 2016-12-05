# --- Part Two ---
#
# Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the
# first location you visit twice.
#
# For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.
#
# How many blocks away is the first location you visit twice?

f = open('day1_1_input.txt', 'r')
data = f.read().split(',')

x = 0
y = 0
# Orientations: N = 0, E = 1, S = 2, W = 3
# Turns: L = -1, R = 1
orientation = 0

points = set()

# Track all the line segments so far so we can find the first intersection
# Segments are stored as point pairs: [[x1, y1], [x2, y2]]
segments = []
found = False
step_count = 0

for step in data:
    step = step.strip()
    direction = step[0]
    distance = int(step[1:])

    old_x = x
    old_y = y

    # Compute the new orientation
    if direction == 'R':
        orientation = (orientation + 1) % 4
    else:
        orientation = (orientation - 1) % 4



    # Compute the motion
    if orientation == 0:
        while distance > 0:
            y += 1
            distance -= 1
            t = tuple([x, y])
            if t in points:
                print "Found! {0}".format(t)
                print "Distance is {0}".format(abs(t[0]) + abs(t[1]))
                found = True
                break
            else:
                points.add(t)
    elif orientation == 1:
        while distance > 0:
            x += 1
            distance -= 1
            t = tuple([x, y])
            if t in points:
                print "Found! {0}".format(t)
                print "Distance is {0}".format(abs(t[0]) + abs(t[1]))
                found = True
                break
            else:
                points.add(t)
    elif orientation == 2:
        while distance > 0:
            y -= 1
            distance -= 1
            t = tuple([x, y])
            if t in points:
                print "Found! {0}".format(t)
                print "Distance is {0}".format(abs(t[0]) + abs(t[1]))
                found = True
                break
            else:
                points.add(t)
    else:
        while distance > 0:
            x -= 1
            distance -= 1
            t = tuple([x, y])
            if t in points:
                print "Found! {0}".format(t)
                print "Distance is {0}".format(abs(t[0]) + abs(t[1]))
                found = True
                break
            else:
                points.add(t)

    if found:
        break


    # step_count += 1
    # print "Step Count is {0}".format(step_count)
    # print "Segment Count is {0}".format(len(segments))
    #
    # # Check if walking from [old_x, old_y] to [x, y] will intersect with any past segments
    # for segment in segments:
    #     point1 = segment[0]
    #     point2 = segment[1]
    #
    #
    #     start_x = min(point1[0], point2[0])
    #     stop_x = max(point1[0], point2[0])
    #
    #     start_y = min(point1[1], point2[1])
    #     stop_y = max(point1[1], point2[1])
    #
    #     print "Point1: {0}".format(point1)
    #     print "Point2: {0}".format(point2)
    #     print "[old_x, old_y]: {0}".format([old_x, old_y])
    #     print "[x, y]: {0}".format([x, y])
    #
    #     if orientation == 0 or orientation == 2:
    #         assert old_x == x
    #
    #         for i in range(min(old_y, y) + 1, max(old_y, y) + 1):
    #             if start_x <= x and x <= stop_x and \
    #                 start_y <= i and i <= stop_y:
    #                 print "Found!"
    #                 print abs(x) + abs(i)
    #                 found = True
    #                 break
    #
    #     else:
    #         assert old_y == y
    #         for i in range(min(old_x, x) + 1, max(old_x, x) + 1):
    #             if start_x <= i and i <= stop_x and \
    #                 start_y <= y and y <= stop_y:
    #                 print "Found!"
    #                 print abs(i) + abs(y)
    #                 found = True
    #                 break
    #
    #     if found:
    #         break
    #
    # if found:
    #     break
    #
    # # Store the new segment in the list of segments
    # segments.append([[old_x, old_y], [x, y]])


#distance = abs(x) + abs(y)
#print distance
if not found:
    print "No intersection found"

