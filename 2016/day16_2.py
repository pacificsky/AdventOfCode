# http://adventofcode.com/2016/day/16

DISK_SIZE = 35651584
INITIAL_INPUT = "01111001100111011"

#DISK_SIZE = 20
#INITIAL_INPUT = "10000"



def main():
    data = [int(x) for x in INITIAL_INPUT]

    while len(data) < DISK_SIZE:
        # inverse while copying
        clone = [1 - bit for bit in data]
        clone.reverse()
        data = data + [0] + clone

    data = data[:DISK_SIZE]
    assert len(data) == DISK_SIZE

    # Initialize checksum with the same info as data
    checksum = [x for x in data]

    while True:
        index = 0
        final_checksum = []
        while index < (len(checksum) - 1):
            if checksum[index] == checksum[index + 1]:
                final_checksum.append(1)
            else:
                final_checksum.append(0)

            index += 2

        checksum = final_checksum
        # Repeat if length is even
        if len(checksum) % 2 == 1:
            break

    # checksum now has the final value
    str_checksum = ""
    for x in checksum:
        str_checksum += str(x)

    print str_checksum







main()