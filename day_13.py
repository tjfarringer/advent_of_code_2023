# from icecream import ic
import numpy as np
from time import perf_counter
import time
import math
# . => ash
# # => rock

# goal:  want to find where the mirrors are
# Add up the number of columns to the left of each vertical line of reflection
# + (100 * #-rows-above-each-horizontal line of reflection)


def check_row_entries(puzzle, r_id, comp_r_id, line_id):
    num_diff = 0
    for e_id in range(0, len(puzzle[r_id])):
        if puzzle[r_id][e_id] != puzzle[comp_r_id][e_id]:
            num_diff += 1
    return num_diff


def check_col_entries(puzzle, c_id, comp_c_id):
    num_diff = 0

    for r_id in range(0, len(puzzle)):
        if puzzle[r_id][c_id] != puzzle[r_id][comp_c_id]:
            num_diff += 1
    return num_diff


def find_horizontal_reflection_line(puzzle, start, target=0):
    for line_id, reflection_line in enumerate(puzzle):
        num_differences = 0
        if line_id <= start:
            continue
        num_above = line_id
        num_below = len(puzzle)-1-line_id
        compare_offset = min(num_above, num_below-1)
        if line_id == 3:
            pass
        if num_below == 0:
            # last row cannot be a line
            continue

        # Check the next row down
        num_differences += check_row_entries(puzzle,
                                             line_id, line_id+1, line_id)
        if num_differences <= target:
            for r_id in range(1, compare_offset+1):
                num_differences += check_row_entries(puzzle,
                                                     line_id-r_id, line_id+r_id+1, line_id)
        if num_differences == target:
            return line_id


def find_col_ref_line(puzzle, start, target=0):

    for col_id in range(len(puzzle[0])):
        num_differences = 0
        if col_id <= start:
            continue
        num_left = col_id
        num_right = len(puzzle[0])-1-col_id
        compare_offset = min(num_left, num_right-1)
        if num_right == 0:
            # last col cannot be a line
            continue
        num_differences += check_col_entries(puzzle, col_id, col_id+1)
        if num_differences <= target:
            for c_id in range(1, compare_offset+1):
                num_differences += check_col_entries(
                    puzzle, col_id-c_id, col_id+c_id+1)
        if num_differences == target:
            return col_id


def day_13(path, target=0):
    answer = 0
    data = []
    with open(path, "r") as f:
        lines = f.read().splitlines()
        for i, line in enumerate(lines):
            if i == 0 or line == "":
                data.append([])

            if line == "":
                continue

            data[-1].append(list(line))

    for p_id, puzzle in enumerate(data):
        col_id = find_col_ref_line(puzzle, -5, target)
        print(f'puzzle: {p_id}')
        while col_id is not None:
            if (col_id+1):
                answer += col_id+1
            col_id = find_col_ref_line(puzzle, col_id, target)

        row_id = find_horizontal_reflection_line(puzzle, -5, target)
        while row_id is not None:
            if (row_id+1):
                answer += (100*(row_id+1))
            row_id = find_horizontal_reflection_line(
                puzzle, row_id, target)

    return answer


start_time = time.time()
# print(day_13("./inputs/day_13_sample.txt", target=0))
# part 1: 43614
# part 2: 36771
print(day_13("./inputs/day_13_input.txt", target=1))
print("--- %s seconds ---" % (time.time() - start_time))
