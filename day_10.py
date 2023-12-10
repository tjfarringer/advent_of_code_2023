import time

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# One large continuous loop
# Some pipes aren't connected to the loop


# Goal:  find the tile farthest from the starting position (S)
# i.e. longest number of steps along the loop, regardless of which way around the loop the animal went
# north, east, south, west
# will need to check positive and the negative direction
pipe_dictionary = {
    "|": (1, 0, 1, 0),
    "-": (0, 1, 0, 1),
    "L": (1, 1, 0, 0),  # this should be either up/down OR left/right
    "J": (1, 0, 0, 1),
    "7": (0, 0, 1, 1),
    "F": (0, 1, 1, 0)
}


def find_start_position(grid):
    for l_idx, line in enumerate(grid):
        for e_idx, entry in enumerate(line):
            # print(f'line: {line}. entry : {entry}')
            if entry == "S":
                return (l_idx, e_idx)


def find_path_starts(grid, starting_position):
    path_starts = []
    num_lines = len(grid)
    num_entries = len(grid[0])
    # start with the north point
    if starting_position[0]-1 > 0 and grid[starting_position[0]-1][starting_position[1]] in pipe_dictionary.keys():
        path_starts.append((starting_position[0]-1, starting_position[1]))
    # east point
    if starting_position[1]+1 < num_lines and grid[starting_position[0]][starting_position[1]-1] in pipe_dictionary.keys():
        path_starts.append((starting_position[0], starting_position[1]-1))
    # west point
    if starting_position[1]+1 < num_entries and grid[starting_position[0]][starting_position[1]+1] in pipe_dictionary.keys():
        path_starts.append((starting_position[0], starting_position[1]+1))
    # south point
    if starting_position[0]+1 < num_entries and grid[starting_position[0]+1][starting_position[1]] in pipe_dictionary.keys():
        path_starts.append((starting_position[0]+1, starting_position[1]))

    return path_starts


def follow_path(grid, point, previous_points):
    # we should know that the point is in the dict
    point_action = pipe_dictionary[grid[point[0]][point[1]]]
    prev_point = previous_points[len(previous_points)-1]

    # north, east, south, west
    for x_idx, x in enumerate(point_action):
        if x == 0:
            continue
        elif x == 1:
            if x_idx == 0:
                # check north
                next_point = (point[0]-1, point[1])
                if next_point != prev_point:
                    return next_point
            elif x_idx == 1:
                # check east
                next_point = (point[0], point[1]+1)
                if next_point != prev_point:
                    return next_point
            elif x_idx == 2:
                # check south
                next_point = (point[0]+1, point[1])
                if next_point != prev_point:
                    return next_point
            elif x_idx == 3:
                # check west
                next_point = (point[0], point[1]-1)
                if next_point != prev_point:
                    return next_point


def day_10(path, part_one=False):
    num_steps = []
    contained_squares = 0
    # Steps:
    # 1 -- Find S and set that as the starting point
    # 2 -- search all neighboring tiles around S
    # IT seems like no pipe can connect multiple ways -- other than S
    # 3 -- repeat step 2 until we hit ground or land back at S
    # Keep track of the visited squares (indx, indx) in a list
    with open(path, "r") as f:
        grid = [l.strip() for l in f]

    # print(grid)
    starting_position = find_start_position(grid)
    path_starts = find_path_starts(grid, starting_position)

    # curr_point = path_starts[1]
    for curr_point in path_starts:
        # print(f'checking: {curr_point}')
        previous_points = []
        previous_points.append(starting_position)
        # previous_points.append(next_point)
        # Loop until you find the cycle
        while grid[curr_point[0]][curr_point[1]] != "S":
            next_point = follow_path(grid, curr_point, previous_points)
            previous_points.append(curr_point)
            curr_point = next_point

        num_steps.append(len(previous_points)//2)

    print(previous_points)

    # Part 2:
    entry_limit = len(grid[0])
    line_limit = len(grid)

    contained_squares = 0
    for x, line in enumerate(grid):
        for y, c in enumerate(line):
            if (x, y) in previous_points:
                continue

            crosses = 0
            x2, y2 = x, y

            while x2 < line_limit and y2 < entry_limit:
                c2 = grid[x2][y2]
                if (x2, y2) in previous_points and c2 != "L" and c2 != "7":
                    crosses += 1
                x2 += 1
                y2 += 1

            if crosses % 2 == 1:
                contained_squares += 1

    print(f'Part 1: {max(num_steps)}')
    print(f'Part 2: {contained_squares}')


# part 1: 6806
# part 2: 449
start_time = time.time()
print(day_10("day_10_sample.txt", part_one=False))
print("--- %s seconds ---" % (time.time() - start_time))
