from queue import Queue
from queue import PriorityQueue
from copy import deepcopy
import time
# Do not hit the same square twice
# What is the longest path you can make?

# Node queue
# ( node-id, steps-so-far, list(visited-nodes) )

# Pick node with the longest steps-so-far


def get_options(grid, cur_line, cur_entry, part_two):
    # Actually he can only go N, S, E, or W
    if not part_two:
        if grid[cur_line][cur_entry] in ['>']:
            options = [(cur_line, cur_entry+1)]
        elif grid[cur_line][cur_entry] in ['<']:
            options = [(cur_line, cur_entry-1)]
        elif grid[cur_line][cur_entry] in ['^']:
            options = [(cur_line - 1, cur_entry)]
        elif grid[cur_line][cur_entry] in ['v']:
            options = [(cur_line+1, cur_entry)]

        return options

    if grid[cur_line][cur_entry] in ['.', '>', '<', '<', 'v']:
        options = [(cur_line-1, cur_entry), (cur_line+1, cur_entry),
                   (cur_line, cur_entry-1), (cur_line, cur_entry+1)]

    return options


def check_neighbors(cur_node, grid, node_queue, end, valid_paths, distance_dict, part_two):
    priority = cur_node[0]
    cur_line = cur_node[1]
    cur_entry = cur_node[2]
    prev_path = cur_node[3]

    options = get_options(grid, cur_line, cur_entry, part_two)

    for o in options:
        new_path = deepcopy(prev_path)
        if o in prev_path:
            continue
            # return True
        elif o == end:
            new_path.append((o[0], o[1]))
            valid_paths.append(new_path)
            # return True
        elif o[0] < 0 or o[0] >= len(grid) or o[1] < 0 or o[1] >= len(grid[0]):
            continue
        elif grid[o[0]][o[1]] in ['.', '>', '<', '<', 'v']:
            new_path.append((o[0], o[1]))
            # If this is the longest path to hit this tile then continue searching
            # otherwise you can stop searching
            # if distance_dict.get((o[0], o[1]), 0) < len(new_path):
            priority = -1*len(new_path)
            node_queue.put((priority, o[0], o[1], new_path))
            distance_dict[o[0], o[1]] = len(new_path)
            # else:
            #     paths_stopped += 1
            #     print(f'stopped')


def day_23(path, part_two=False):
    # node_queue = Queue()
    node_queue = PriorityQueue()
    valid_paths = []
    max_path = 0
    distance_dict = {}
    # Creating our data structures
    with open(path, "r") as f:
        grid = [list(line.strip())
                for line in f.readlines()]

    start = grid[0].index('.')
    end = (len(grid)-1, grid[len(grid)-1].index('.'))
    node_queue.put((-1, 0, start, [(0, start)]))
    distance_dict[(0, start)] = 0

    while not node_queue.empty():
        if node_queue.qsize() > 1:
            pass
        cur_node = node_queue.get()
        # if cur_node[1] == 5 and cur_node[2] == 3:
        #     pass
        if check_neighbors(cur_node, grid, node_queue, end, valid_paths, distance_dict, part_two):
            break

    if len(valid_paths) > 0:
        for path in valid_paths:
            if len(path)-1 > max_path:
                # Subtract 1 to ignore the starting position
                max_path = len(path)-1

    print(
        f'Part 1 answer: {max_path} num paths: {len(valid_paths)}')


start_time = time.time()
# Part 1 answer: 2238.. right now 134 seconds
# day_23("./inputs/day_23_sample.txt", part_two=True)
day_23("./inputs/day_23_input.txt", part_two=True)
print("--- %s seconds ---" % (time.time() - start_time))
