f = open('day_1_input.txt', 'r')
data = f.read()
floor = 0
first_basement_position = 1
basement_found = False
for letter in data:
    if letter == '(':
        floor += 1
    else:
        floor -= 1
    if not basement_found:
        if floor == -1:
            basement_found = True
            print "First basement position", first_basement_position
        else:
            first_basement_position += 1

print floor




