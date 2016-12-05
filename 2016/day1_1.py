# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get
# - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work
# them out further.
#
# The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then,
# follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of
# blocks, ending at a new intersection.
#
# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the
# destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the
# destination?
#
# For example:
#
# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away. R2, R2, R2 leaves you 2 blocks due South
# of your starting position, which is 2 blocks away. R5, L5, R5, R3 leaves you 12 blocks away. How many blocks away is
# Easter Bunny HQ?


f = open('day1_1_input.txt', 'r')
data = f.read().split(',')

x = 0
y = 0
# Orientations: N = 0, E = 1, S = 2, W = 3
# Turns: L = -1, R = 1
orientation = 0

for step in data:
    step = step.strip()
    direction = step[0]
    distance = int(step[1:])

    # Compute the new orientation
    if direction == 'R':
        orientation = (orientation + 1) % 4
    else:
        orientation = (orientation - 1) % 4

    # Compute the motion
    if orientation == 0:
        y += distance
    elif orientation == 1:
        x += distance
    elif orientation == 2:
        y -= distance
    else:
        x -= distance


distance = abs(x) + abs(y)
print distance

