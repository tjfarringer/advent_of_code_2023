from collections import defaultdict, Counter, deque
from math import gcd
from copy import deepcopy
import re
import sys
import time
import functools
from memoization import cached
from tqdm import tqdm

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


def roll_east(grid, r_id, e_id, east=True):
    new_entry = e_id
    # start from the row and head north
    if east:
        for x in range(e_id+1, len(grid[0])):
            # if grid[x][e_id] == ".":
            #     # then swap
            #     grid[x][e_id] = round_rocks
            #     grid[r_id][e_id] = "."
            if grid[r_id][x] != ground:
                # if hit block then go back one row
                new_entry = x-1
                break
            else:
                new_entry = x
    else:
        # otherwise we are going west
        for x in reversed(range(0, e_id)):
            # if grid[x][e_id] == ".":
            #     # then swap
            #     grid[x][e_id] = round_rocks
            #     grid[r_id][e_id] = "."
            if grid[r_id][x] != ground:
                # if hit block then go back one row
                new_entry = x+1
                break
            else:
                new_entry = x
    if new_entry != e_id:
        grid[r_id][new_entry] = round_rocks
        grid[r_id][e_id] = ground


def roll_north(grid, r_id, e_id, north=True):
    new_row = r_id
    # start from the row and head north
    if north:
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
    else:
        # otherwise we are going south
        for x in range(r_id+1, len(grid)):
            # if grid[x][e_id] == ".":
            #     # then swap
            #     grid[x][e_id] = round_rocks
            #     grid[r_id][e_id] = "."
            if grid[x][e_id] != ground:
                # if hit block then go back one row
                new_row = x-1
                break
            else:
                new_row = x
    if new_row != r_id:
        grid[new_row][e_id] = round_rocks
        grid[r_id][e_id] = ground


def calculate_load(grid):
    total_load = 0
    for row_id, row in enumerate(grid):
        for entry_id, entry in enumerate(row):
            if entry == round_rocks:
                total_load += len(grid) - row_id

    return total_load


def turn_grid(grid, direction):
    # grid = grid[0]
    if direction in ["N", "W"]:
        for row_id, row in enumerate(grid):
            for entry_id, entry in enumerate(row):
                if entry == round_rocks:
                    if row_id == 1 and entry_id == 2:
                        pass
                    if direction == "N":
                        roll_north(grid, row_id, entry_id, north=True)
                    elif direction == "W":
                        if row_id == 6 and entry_id == 2:
                            pass
                        roll_east(grid, row_id, entry_id, east=False)
    elif direction in ["S"]:
        for row_id in reversed(range(0, len(grid))):
            for entry_id in range(0, len(grid[row_id])):
                if grid[row_id][entry_id] == round_rocks:
                    roll_north(grid, row_id, entry_id, north=False)
    elif direction in ["E"]:
        for row_id, row in enumerate(grid):
            for entry_id in reversed(range(0, len(grid[row_id]))):
                if grid[row_id][entry_id] == round_rocks:
                    roll_east(grid, row_id, entry_id, east=True)
    return grid


def day_14(path, cycles=1):
    # Cycle: North, West, South, East
    directions = ["N", "W", "S", "E"]
    with open(path, "r") as f:
        grid = [list(l.strip()) for l in f]

    for turn in tqdm(range(1, cycles*4+1)):
        direction = directions[(turn-1) % len(directions)]
        # print(f'turning {direction}')
        grid_tuple = tuple(grid)
        grid = turn_grid(grid_tuple, direction)

    # return calculate_load(grid)
    return grid


# part 1: 108759
# part 2: 89089
start_time = time.time()
# according to reddit 1B should be the same as 1,000 cycles
# print(day_14("./inputs/day_14_input.txt", cycles=1000))
talmadge_grid = day_14("./inputs/day_14_input.txt", cycles=1000)
# print(day_14("./inputs/day_14_sample.txt", cycles=1000))

print("--- %s seconds ---" % (time.time() - start_time))
