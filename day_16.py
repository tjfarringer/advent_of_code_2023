import time
# empty space (.)
# mirrors (/ and \)
# splitters (| and -).

# each tile on the grid converts some of the beam's light into heat

# The beam enters in the top-left corner from the left and heading to the right.

# If the beam encounters empty space (.), it continues in the same direction.
# If the beam encounters a mirror (/ or \),
# the beam is reflected 90 degrees depending on the angle of the mirror.
#  For instance, a rightward-moving beam that encounters a / mirror
# would continue upward in the mirror's column, while a rightward-moving beam that
# encounters a \ mirror would continue downward from the mirror's column.

# If the beam encounters the pointy end of a splitter (| or -),
# the beam passes through the splitter as if the splitter were empty space.
# For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.

# If the beam encounters the flat side of a splitter (| or -),
# the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing.
# For instance, a rightward-moving beam that encounters a | splitter would split into
# two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.

# A tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.

# Goal:  How many tiles are energized?


# num-positions-right, num-pos-down, new-direction
# this is the additional squares to move
move_map = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1)
}

redirect_map = {
    '\\': {
        'R': [(0, 1, 'D')],
        'L': [(0, -1, 'U')],
        'U': [(-1, 0, 'L')],
        'D': [(1, 0, 'R')]
    },
    '|': {
        'R': [(0, -1, 'U'), (0, 1, 'D')],
        'L': [(0, -1, 'U'), (0, 1, 'D')],
        'U': [(0, -1, 'U')],
        'D': [(0, 1, 'D')]
    },
    '/': {
        'R': [(0, -1, 'U')],
        'L': [(0, 1, 'D')],
        'U': [(1, 0, 'R')],
        'D': [(-1, 0, 'L')]
    },
    '-': {
        'R': [(1, 0, 'R')],
        'L': [(-1, 0, 'L')],
        'U': [(-1, 0, 'L'), (1, 0, 'R')],
        'D': [(-1, 0, 'L'), (1, 0, 'R')]
    }
}


def append_beam(new_line, new_entry, new_dir, grid, beams, visited_tiles):
    if (new_line, new_entry, new_dir) not in beams and (new_line, new_entry, new_dir) not in visited_tiles:
        if new_line < 0 or new_line >= len(grid) or new_entry < 0 or new_entry >= len(grid[0]):
            return beams
        else:
            # line, entry, new-direction
            beams.append((new_line, new_entry, new_dir))

    return beams


def day_16(path, part_two):
    # Creating our grid
    with open(path, "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    max_val = 0
    starting_positions = []

    if part_two:
        # top row
        for x in range(0, len(grid[0])):
            starting_positions.append((0, x, 'D'))
        # bottom row
        for x in range(0, len(grid[0])):
            starting_positions.append((len(grid)-1, x, 'U'))
        # left side
        for x in range(0, len(grid)):
            starting_positions.append((x, 0, 'R'))
        # right side
        for x in range(0, len(grid)):
            starting_positions.append((x, len(grid[0])-1, 'L'))
    else:
        starting_positions = [(0, 0, 'R')]

    for x in starting_positions:
        # point and direction
        beams = []
        # add starting position
        beams.append(x)
        energized_tiles = []
        visited_tiles = []
        # visited_tiles.append((0, 1, 'R'))

        while len(beams) > 0:
            curr_beam = beams.pop()
            # capture the base case
            line_num = curr_beam[0]
            entry_num = curr_beam[1]
            direction = curr_beam[2]

            visited_tiles.append((line_num, entry_num, direction))
            energized_tiles.append((line_num, entry_num))

            if curr_beam[0] == 6 and curr_beam[1] == 4:
                pass

            # if the beam start tile is special then edit that case
            if grid[curr_beam[0]][curr_beam[1]] in ["\\", "|", "/", "-"]:
                nxt_symbol = grid[line_num][entry_num]
                for new_beam in redirect_map[nxt_symbol][direction]:
                    new_line = line_num + new_beam[1]
                    new_entry = entry_num + new_beam[0]
                    new_direction = new_beam[2]

                    beams = append_beam(new_line, new_entry,
                                        new_direction, grid, beams, visited_tiles)

                # Does this go to the next beam?
                continue
            else:
                # otherwise we move in the direction
                line_num += move_map[direction][1]
                entry_num += move_map[direction][0]
                beams = append_beam(line_num, entry_num,
                                    direction, grid, beams, visited_tiles)

        if len(set(energized_tiles)) > max_val:
            max_val = len(set(energized_tiles))

    print(f'part 2 answer: {max_val}')


start_time = time.time()

# day_16("./inputs/day_16_sample.txt", part_two=True)
day_16("./inputs/day_16_input.txt", part_two=True)
# part 2 -- 266 seconds.  Ans: 7488
print("--- %s seconds ---" % (time.time() - start_time))
