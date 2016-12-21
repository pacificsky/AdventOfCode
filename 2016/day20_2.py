# http://adventofcode.com/2016/day/20

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
    allowed_count = 0
    for i in range(len(data)):
        value = data[i]
        assert LOWER_BOUND <= value[0] <= UPPER_BOUND
        assert LOWER_BOUND <= value[1] <= UPPER_BOUND

        if ip_address < value[0]:
            # Found some IP addresses that are allowed
            allowed_count += (value[0] - ip_address)

        if ip_address <= value[1]:
            ip_address = value[1] + 1

    if allowed_count > 0:
        print "Done! {0} allowed IP addresses".format(allowed_count)


main()

