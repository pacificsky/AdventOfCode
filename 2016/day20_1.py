# http://adventofcode.com/2016/day/20
from color import Color
from color import color_print

LOWER_BOUND = 0
UPPER_BOUND = 4294967295


def main():
    f = open("day20_1_input.txt", "r")
    data = [line.strip().strip("\n") for line in f]
    f.close()

    for i in range(len(data)):
        inputs = data[i].split('-')
        data[i] = (int(inputs[0]), int(inputs[1]))

    data.sort(key=lambda x: x[0])

    ip_address = 0
    index = 0
    for i in range(len(data)):
        value = data[i]
        if ip_address < value[0]:
            index = i
            break
        elif ip_address <= value[1]:
            ip_address = value[1] + 1


    if ip_address <= 4294967295:
        print "Done! Found ip address {0}".format(ip_address)
        printed = False
        for i in range(max(LOWER_BOUND, index - 10), min(UPPER_BOUND, index + 10)):
            if ip_address < data[i][0] and not printed:
                color_print(Color.BLUE, "-- {0} --".format(ip_address))
                printed = True
            print "{0} - {1}".format(data[i][0], data[i][1])


main()

