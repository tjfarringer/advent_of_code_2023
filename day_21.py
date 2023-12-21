from queue import Queue
import time


# which garden plots he can reach with exactly his remaining 64 steps
# starting position (S), garden plots (.), and rocks (#)

# Maybe find min and if min is a multiple of the num-steps then that'd work?

def check_neighbors(tile, garden, tile_queue, steps_threshold, exact_distance, visited):
    cur_line = tile[0]
    cur_entry = tile[1]
    cur_steps = tile[2]

    # If we've been here already skip it
    if (cur_line, cur_entry, cur_steps) in visited:
        return
    else:
        visited.add((cur_line, cur_entry, cur_steps))

    # Actually he can only go N, S, E, or W
    options = [(cur_line-1, cur_entry), (cur_line+1, cur_entry),
               (cur_line, cur_entry-1), (cur_line, cur_entry+1)]
    for o in options:
        if cur_steps+1 > steps_threshold:
            break
        elif o[0] < 0 or o[0] >= len(garden) or o[1] < 0 or o[1] >= len(garden[0]):
            continue
        elif garden[o[0]][o[1]] == "#":
            continue
        elif (cur_steps+1) == steps_threshold:
            exact_distance.add((o[0], o[1]))
        else:
            tile_queue.put((o[0], o[1], cur_steps+1))


def day_21(path, steps):
    # (line_i, e_i): {steps-to-get}
    tile_queue = Queue()
    exact_distance = set()
    visited = set()

    # Creating our data structures
    with open(path, "r") as f:
        garden = [list(line.strip())
                  for line in f.readlines()]

    # Find start position
    for l_i, line in enumerate(garden):
        for e_i, entry in enumerate(line):
            if entry == "S":
                # tile_dict[(l_i, e_i)] = 0
                tile_queue.put((l_i, e_i, 0))

    # tile, grid, tile_dict
    while not tile_queue.empty():
        tile_to_chk = tile_queue.get()
        check_neighbors(tile_to_chk, garden,
                        tile_queue, steps, exact_distance, visited)

    print(f'Part one answer: {len(exact_distance)}')


start_time = time.time()
# day_21("./inputs/day_21_sample.txt", steps=64)
day_21("./inputs/day_21_input.txt", steps=64)
print("--- %s seconds ---" % (time.time() - start_time))
