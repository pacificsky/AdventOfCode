# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of
# three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.
#
# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:
#
# 101 301 501 102 302 502 103 303 503 201 401 601 202 402 602 203 403 603 In your puzzle input, and instead reading by
# columns, how many of the listed triangles are possible?

import numpy

total = 0
matching = 0
set_count = 0
data = []

f = open('day3_1_input.txt', 'r')
for line in f:
    line = line.rstrip().rstrip('\n')
    sides = [int(x) for x in line.split()]
    # print sides
    data.append(sides)
    set_count += 1
    if set_count == 3:
        matrix = numpy.array(data)
        matrix = matrix.transpose()

        for triangle in matrix:
            a = triangle[0]
            b = triangle[1]
            c = triangle[2]

            if a + b > c and b + c > a and c + a > b:
                matching += 1

        data = []
        set_count = 0


#print total
print matching

