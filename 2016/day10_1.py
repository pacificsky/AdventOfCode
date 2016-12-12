# http://adventofcode.com/2016/day/10
import parse


def get_bot(bots, bot_id):
    if bot_id in bots:
        return bots[bot_id]
    bot = {"values": [], "actions": []}
    bots[bot_id] = bot
    return bot


def populate_inputs(bots, input_data):
    bot = get_bot(bots, input_data["bot_id"])
    input_value = input_data["input_value"]
    assert len(bot["values"]) < 2
    bot["values"].append(input_value)
    if len(bot["values"]) == 2:
        bot["values"].sort()

        if bot["values"][0] == 17 and bot["values"][1] == 61:
            print "Answer bot ID: {0}".format(input_data["bot_id"])


def populate_outputs(outputs, output_data):
    output = get_bot(outputs, output_data["bot_id"])
    output_value = output_data["output_value"]
    output["values"].append(output_value)


def populate_actions(bots, input_data):
    bot = get_bot(bots, input_data["bot_id"])
    action_data = input_data["action_data"]
    bot["actions"].append(action_data)


def process_action(bots, outputs, bot):
    actions = bot["actions"]
    values = bot["values"]
    if len(values) < 2 or len(actions) == 0:
        return 0

    action = actions[0]

    if action["low_target"] == "bot":
        populate_inputs(bots, {"bot_id": action["low_target_id"], "input_value": values[0]})

    else:
        assert action["low_target"] == "output"
        populate_outputs(outputs, {"bot_id": action["low_target_id"], "output_value": values[0]})

    if action["high_target"] == "bot":
        populate_inputs(bots, {"bot_id": action["high_target_id"], "input_value": values[1]})

    else:
        assert action["high_target"] == "output"
        populate_outputs(outputs, {"bot_id": action["high_target_id"], "output_value": values[1]})

    # Remove the processed action and values
    bot["actions"].remove(action)
    bot["values"] = []
    return 1


def execute(bots, outputs):
    count = 0
    current_items = bots.values()
    for bot in current_items:
        count += process_action(bots, outputs, bot)

    return count


# Parse the input
def parse_input(item):
    result = parse.parse("value {:d} goes to bot {:d}", item)
    if result:
        return {"function": populate_inputs, "data": {"bot_id": result[1], "input_value": result[0]}}

    result = parse.parse("bot {:d} gives low to {:w} {:d} and high to {:w} {:d}", item)
    if result:
        result_data = {"function": populate_actions}
        data = {"bot_id": result[0]}

        action_data = {}
        action_data["low_target"] = result[1]
        action_data["low_target_id"] = result[2]
        action_data["high_target"] = result[3]
        action_data["high_target_id"] = result[4]

        data["action_data"] = action_data
        result_data["data"] = data
        return result_data

    assert False, "Unable to parse input {0}".format(item)


def main():

    # bots = { bot_id: bot_data }
    # bot_id = INTEGER
    # bot_data = { "values": [low_value_INTEGER, high_value_INTEGER], "instr": bot_instr }
    # bot_instr = [

    bots = {}
    outputs = {}
    to_remove = []

    f = open("day10_1_input.txt", "r")
    data = [line.strip().strip("\n") for line in f]
    f.close()

    outer_loop_count = 0

    while len(data) > 0:
        outer_loop_count += 1
        for item in data:
            parse_result = parse_input(item)
            # Execute either the assignment of input of population of actions
            parse_result["function"](bots, parse_result["data"])

            # See if any bots are ready to execute
            inner_loop_count = 0
            while execute(bots, outputs) > 0:
                inner_loop_count += 1
                #print "Inner loop count: {0}".format(inner_loop_count)
                continue

            to_remove.append(item)

        # After this pass is complete, remove all items from data that have been processed
        for item in to_remove:
            data.remove(item)

        print "Outer Loop Count: {0}".format(outer_loop_count)
        # Answer for part 2 can be inferred by looking at the outputs array
        print outputs


main()

