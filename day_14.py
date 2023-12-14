# O => rounded rock that would move
# # => fixed rock
# . => empty space

# Only for rounded rocks!!
# Amount of load: equal to the # rows from the rock to the south edge of the platform
# Including the row the rock si on


# Tilt platform so all rounded rocks roll north
# Goal: what is the total load on the north support beams?

round_rocks = "O"
ground = "."


def roll_north(grid, r_id, e_id):
    new_row = r_id
    # start from the row and head north
    for x in reversed(range(0, r_id)):
        # if grid[x][e_id] == ".":
        #     # then swap
        #     grid[x][e_id] = round_rocks
        #     grid[r_id][e_id] = "."
        if grid[x][e_id] != ground:
            # if hit block then go back one row
            new_row = x+1
            break
        else:
            new_row = x
    if new_row != r_id:
        grid[new_row][e_id] = round_rocks
        grid[r_id][e_id] = "."


def calculate_load(grid):
    total_load = 0
    for row_id, row in enumerate(grid):
        for entry_id, entry in enumerate(row):
            if entry == "O":
                total_load += len(grid) - row_id

    return total_load


def day_14(path):
    with open(path, "r") as f:
        grid = [list(l.strip()) for l in f]

    for row_id, row in enumerate(grid):
        for entry_id, entry in enumerate(row):
            if entry == round_rocks:
                if row_id == 1 and entry_id == 2:
                    pass
                roll_north(grid, row_id, entry_id)

    return calculate_load(grid)


print(day_14("./inputs/day_14_input.txt"))
# for x in reversed(range(0, 4)):
#     print(x)
