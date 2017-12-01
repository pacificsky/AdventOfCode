# http://adventofcode.com/2016/day/21
import parse

# swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
def swap_position(input_str, pos1, pos2):


# swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the
# string).
def swap_letters(input_str, letter1, letter2):


# rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd
# into dabc.
def rotate(input_str, value):



# rotate based on position of letter X means that the whole string should be rotated to the right based on the index of
# letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined,
# rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the
# index was at least 4.
def rotate_by_letter(data, letter):

# reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y)
# should be reversed in order.
def reverse_span(data, pos1, pos2):


# move position X to position Y means that the letter which is at index X should be removed from the string, then inserted
# such that it ends up at index Y.
def move_letter(data, pos1, pos2):



RULES = { parse.compile("rotate {:w} {:d} steps"): rotate,
          parse.compile("swap position {:d} with position {:d}"): swap_position,
          parse.compile("swap letter {:w} with letter {:w}"): swap_letters,
          parse.compile("rotate based on position of letter {:w}"): rotate_by_letter,
          parse.compile("reverse positions {:d} through {:d}"): reverse_span,
          parse.compile("move position {:d} to position {:d}"): move_letter }



def parse(lines):
    instructions = []

    for line in lines:
        found = False
        for rule in RULES:
            result = rule.match(line)
            if result is None:
                continue

            data = [i for i in result]
            instructions.append((RULES[rule], data))
            found = True
            break

        if not found:
            assert False, "Unable to parse: {0}".format(line)

    return instructions


def execute(instruction, input_str):
    command = instruction[0]
    data = instruction[1]
    return command(input_str, data)


def main():
    f = open("day21_1_input.txt", "r")
    lines = [line.strip().strip("\n") for line in f]
    f.close()

    input_str = "abcdefgh"

    instructions = parse(lines)
    for instruction in instructions:
        input_str = execute(instruction, input_str)

    print input_str





main()