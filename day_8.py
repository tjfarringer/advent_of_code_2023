from math import lcm
# Map on how to navigate the desert
# L,R instructions.  Rest describe a network
# AAA => start.  ZZZ => end
# Repeat instructions if you run out
# How many steps until you hit ZZZ?

# num nodes ending in A = num nodes ending in Z
# start at every node ending in A and follow all paths at the same time until they end at nodes that end in Z
# How many steps does it take?


def follow_path(starting_node, ending_nodes, instructions, node_dict):
    instruction_idx = 0
    steps_required = 0
    current_node = starting_node

    while current_node not in ending_nodes:
        current_instruction = instructions[instruction_idx]
        next_node = node_dict[current_node][0] if current_instruction == 'L' else node_dict[current_node][1]
        instruction_idx = (instruction_idx+1) % len(instructions)
        current_node = next_node
        steps_required += 1

    return steps_required


def day_8(path, part_one=False):
    starting_nodes = []
    ending_nodes = []
    required_counts = []
    node_dict = {}

    with open(path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        instructions = lines[0]
        for x in range(2, len(lines)):
            node_list = lines[x].split('=')
            node_tuple = node_list[1].strip()
            node_tuple = node_tuple.replace("(", "")
            node_tuple = node_tuple.replace(")", "")
            node_tuple = node_tuple.replace(" ", "")
            node_tuple = node_tuple.split(",")
            node_dict[node_list[0].strip()] = (node_tuple[0], node_tuple[1])

    starting_nodes = [node for node in node_dict.keys() if node.endswith('A')]
    ending_nodes = [node for node in node_dict.keys() if node.endswith('Z')]

    # code for part 1
    if part_one:
        # 12643
        return follow_path(
            'AAA', ['ZZZ'], instructions, node_dict)
    # code for part 2
    # Tried brute force but that didn't work.  Found the LCM path via reddit
    for starting_node in starting_nodes:
        required_count = follow_path(
            starting_node, ending_nodes, instructions, node_dict)
        required_counts.append(required_count)

    # 13133452426987
    return lcm(*required_counts)


print(day_8("day_8_input.txt", part_one=True))
