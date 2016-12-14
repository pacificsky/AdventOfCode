# http://adventofcode.com/2016/day/12
import parse

def i_copy(registers, data):
    if data["x"].isdigit():
        registers[data["y"]] = int(data["x"])
    else:
        registers[data["y"]] = registers[data["x"]]

    registers["index"] += 1


def i_inc(registers, data):
    registers[data["x"]] += 1
    registers["index"] += 1


def i_dec(registers, data):
    registers[data["x"]] -= 1
    registers["index"] += 1


def i_jnz(registers, data):
    value = 0
    if data["x"].isdigit():
        value = int(data["x"])
    else:
        value = registers[data["x"]]

    if value != 0:
        assert data["y"].lstrip("-").isdigit()
        offset = int(data["y"])
        registers["index"] += offset
    else:
        registers["index"] += 1


def parse_input(line):
    function = None
    data = None

    result = parse.parse("cpy {} {}", line)
    if result:
        function = i_copy
        data = {"x": result[0], "y": result[1]}

    if not result:
        result = parse.parse("inc {}", line)
        if result:
            function = i_inc
            data = {"x": result[0]}

    if not result:
        result = parse.parse("dec {}", line)
        if result:
            function = i_dec
            data = {"x": result[0]}

    if not result:
        result = parse.parse("jnz {} {}", line)
        if result:
            function = i_jnz
            data = {"x": result[0], "y": result[1]}

    #print line
    assert result
    return {"function": function, "data": data}


def main():

    registers = {"index": 0, "a": 0, "b": 0, "c": 0, "d": 0}

    f = open("day12_1_input.txt", "r")
    data = [line.strip().strip("\n") for line in f]
    f.close()

    print data

    end = len(data)

    while registers["index"] < end:
        index = registers["index"]
        line = data[index]
        instr = parse_input(line)
        # Execute the instruction
        instr["function"](registers, instr["data"])


    print "a:{0}, b:{1}, c:{2}, d:{3}".format(registers["a"], registers["b"], registers["c"], registers["d"])




main()