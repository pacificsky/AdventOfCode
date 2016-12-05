# --- Day 2: I Was Told There Would Be No Math ---
#
# The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the
# dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.
#
# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping
# paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also
# need a little extra paper for each present: the area of the smallest side.
#
# For example:
#
# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of
# slack, for a total of 58 square feet. A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of
# wrapping paper plus 1 square foot of slack, for a total of 43 square feet. All numbers in the elves' list are in feet.
# How many total square feet of wrapping paper should they order?


sqft = 0
ribbon = 0
f = open('day2_1_input.txt', 'r')
# Read line by line
for line in f:
    #print line
    # Split the line using x as the separator
    sides = line.rstrip('\n').split('x')
    #print sides

    # Convert the strings to ints
    sides = [int(x) for x in sides]
    #print sides

    #Calculate the running total of sq ft
    l = sides[0]
    w = sides[1]
    h = sides[2]

    area1 = l*w
    area2 = w*h
    area3 = l*h

    perimeter1 = 2*(l+w)
    perimeter2 = 2*(w+h)
    perimeter3 = 2*(l+h)


    sqft += 2*area1 + 2*area2 + 2*area3
    sqft += min(area1, area2, area3)

    ribbon += min(perimeter1, perimeter2, perimeter3)
    ribbon += l*w*h

print sqft
print ribbon



