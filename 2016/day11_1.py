# http://adventofcode.com/2016/day/11
import itertools
import copy
import Queue
import sys


# state = {"position": current_floor, "floors": {floor_id: floor_state, ...}}
# current_floor: INTEGER
# floor_id: INTEGER
# floor_state = {"chips": [...], "generators": [...]}

def is_final(state):
    current_floor = state["position"]
    floor = state["floors"][current_floor]

    return current_floor == FINAL_FLOOR and len(floor["chips"]) == FINAL_CHIP_COUNT and \
        len(floor["generators"]) == FINAL_GENERATOR_COUNT


def is_valid(state):
    floors = state["floors"]
    for key in floors.iterkeys():
        floor = floors[key]

        chips = floor["chips"]
        generators = floor["generators"]

        if len(chips) > 0 and len(generators) > 0:
            for chip in chips:
                if chip not in generators:
                    return False

    return True


def is_valid_combination(elevator_state):
    if len(elevator_state["chips"]) == 0:
        return True

    if len(elevator_state["generators"]) == 0:
        return True

    chips = elevator_state["chips"]
    generators = elevator_state["generators"]
    for chip in chips:
        if chip not in generators:
            return False

    return True


def generate_combinatorics(floor):
    # Generate the possible elevator states given a valid floor
    input_array = ["chip_" + chip for chip in floor["chips"]]
    input_array.extend(["generator_" + generator for generator in floor["generators"]])
    combinations = list(itertools.combinations(input_array, 1))
    combinations.extend(list(itertools.combinations(input_array, 2)))

    # print combinations

    outputs = []

    for item in combinations:
        chips = []
        generators = []
        for x in item:
            if x.startswith("chip_"):
                chips.append(x.split("_")[1])
            else:
                assert x.startswith("generator_")
                generators.append(x.split("_")[1])

        elevator_state = {"chips": chips, "generators": generators}
        # print elevator_state
        if is_valid_combination(elevator_state):
            outputs.append(elevator_state)

    return outputs


def state_hash(state):
    result = []
    result.append(state["position"])
    floors = state["floors"]
    for x in range(1, 5):
        result.append(sorted(floors[x]["chips"]))
        result.append(sorted(floors[x]["generators"]))

    return str(result)


# Combine global state with elevator state to generate a new global state
def apply(state, seen_states, elevator_state, position):
    state_copy = copy.deepcopy(state)
    # remove items from old position
    old_position = state_copy["position"]
    old_floor = state_copy["floors"][old_position]
    for chip in elevator_state["chips"]:
        old_floor["chips"].remove(chip)
    for generator in elevator_state["generators"]:
        old_floor["generators"].remove(generator)

    # Set up the new state
    state_copy["position"] = position
    floor = state_copy["floors"][position]
    floor["chips"].extend(elevator_state["chips"])
    floor["generators"].extend(elevator_state["generators"])
    if not is_valid(state_copy):
        return None

    state_copy_hash = state_hash(state_copy)
    if state_copy_hash in seen_states:
        return None

    seen_states.add(state_copy_hash)

    return state_copy


def generate(state, seen):
    # Return valid new states that haven't been seen before

    # 1. Generate combinatorics of elevator state and determine valid subset
    current_position = state["position"]
    floor = state["floors"][current_position]

    valid_elevator_states = generate_combinatorics(floor)
    if len(valid_elevator_states) == 0:
        #print "No valid elevator states"
        return []

    #print valid_elevator_states


    # 2. Determine new global state by moving one floor in either direction for each elevator state and check if we've
    # seen it before
    new_positions = []
    if current_position == 1:
        new_positions = [2]
    elif current_position == 4:
        new_positions = [3]
    else:
        new_positions = [current_position - 1, current_position + 1]

    new_states = []
    for elevator_state in valid_elevator_states:
        for position in new_positions:
            valid_position = apply(state, seen, elevator_state, position)
            if valid_position:
                new_states.append(valid_position)

    # Return list of new global states which are valid
    return new_states


def run(seen_states, queue, wins):

    while queue.qsize() > 0:
        item = queue.get()
        iteration = item[0]
        state = item[1]

        #print "Iteration: {0}\r".format(iteration)
        sys.stderr.write("Iteration: {0}\r".format(iteration))

        new_states = generate(state, seen_states)
        if len(new_states) == 0:  # Cant move forward
            continue

        for new_state in new_states:
            if is_final(new_state):
                #wins.append((new_state, iteration + 1))
                print "Finished with iteration = {0}".format(iteration)
                return
            else:
                queue.put((iteration + 1, new_state))

    # stack.append(state)
    #
    # print "Stack depth {0}".format(len(stack))
    # #print "State: {0}".format(state)
    #
    # new_states = generate(state, seen_states)
    # if len(new_states) == 0:  # Cant move forward
    #     # print "Popping stack"
    #     stack.pop()
    #     return
    #
    # for new_state in new_states:
    #     if is_final(new_state):
    #         wins.append((new_state, len(stack) + 1))
    #
    #     else:
    #         run(new_state, seen_states, stack, wins)
    #
    # stack.pop()



FINAL_CHIP_COUNT = 5
FINAL_GENERATOR_COUNT = 5
FINAL_FLOOR = 4


def main():
    # Define the initial state
    floor1 = {"chips": ["promethium"], "generators": ["promethium"]}
    floor2 = {"chips": [], "generators": ["cobalt", "curium", "ruthenium", "plutonium"]}
    floor3 = {"chips": ["cobalt", "curium", "ruthenium", "plutonium"], "generators": []}
    floor4 = {"chips": [], "generators": []}
    state = {"position": 1, "floors": {1: floor1, 2: floor2, 3: floor3, 4: floor4}}

    seen_states = set()
    queue = Queue.Queue()
    wins = []

    queue.put((0, state))
    seen_states.add(state_hash(state))
    run(seen_states, queue, wins)
    print wins





main()
