# --- Day 3: Squares With Three Sides ---
#
# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this
# part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for
# triangles.
#
# Or are they?
#
# The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't
# triangles. You can't help but mark the impossible ones.
#
# In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given
# above is impossible, because 5 + 10 is not larger than 25.
#
# In your puzzle input, how many of the listed triangles are possible?



total = 0
matching = 0


f = open('day3_1_input.txt', 'r')
for line in f:
    line = line.rstrip().rstrip('\n')
    sides = line.split()
    # print sides

    a = int(sides[0])
    b = int(sides[1])
    c = int(sides[2])

    total += 1
    if a + b > c and b + c > a and c + a > b:
        matching += 1

print total
print matching

