# http://adventofcode.com/2016/day/9
import parse


def parse_command(command_buffer):
    return parse.parse("({length:d}x{repeat:d})", command_buffer)

def main():
    f = open("day9_1_input.txt", "r")
    data = f.read().strip()
    f.close()

    output_buffer = ""
    index = 0
    end = len(data)

    print "Length of data is {0}".format(end)

    while index < end:
        current = data[index]
        print "Processing index {0}".format(index)
        print "Current is {0}".format(current)
        # skip whitespace
        assert current != ' '
        if current == '(':
            end_index = data.find(')', index)
            command_buffer = data[index:end_index + 1]
            command = parse_command(command_buffer)
            print "Command buffer is {0}".format(command_buffer)
            print "Command is {0}".format(command)

            length = command['length']
            repeat = command['repeat']
            source = data[end_index + 1:end_index + 1 + length]
            clean_source = source.replace(" ", "")
            for i in range(repeat):
                output_buffer += clean_source

            print "Source is {0}".format(source)

            index = end_index + 1 + length
            continue
        else:
            end_index = data.find('(', index)
            if end_index == -1:  # End of string
                end_index = end

            source = data[index:end_index]
            source = source.replace(" ", "")
            output_buffer += source
            index = end_index
            continue

    print len(output_buffer)

main()