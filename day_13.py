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


def check_row_entries(puzzle, r_id, comp_r_id):
    # for all entries
    for e_id in range(0, len(puzzle[r_id])):
        if puzzle[r_id][e_id] != puzzle[comp_r_id][e_id]:
            return False
    return True


def check_col_entries(puzzle, c_id, comp_c_id):
    for r_id in range(0, len(puzzle)):
        if puzzle[r_id][c_id] != puzzle[r_id][comp_c_id]:
            return False
    return True


def find_horizontal_reflection_line(puzzle, start):
    for line_id, reflection_line in enumerate(puzzle):
        if line_id <= start:
            continue
        num_above = line_id
        num_below = len(puzzle)-1-line_id
        compare_offset = min(num_above, num_below)
        if line_id == 9:
            pass
        if compare_offset == 0:
            if num_below > 0 and check_row_entries(puzzle, line_id, line_id+1):
                return line_id
            else:
                continue

        if check_row_entries(puzzle, line_id, line_id+1):
            # compare_offset -= 1
            compare_offset = min(num_above, (num_below-1))
            if compare_offset == 0:
                # This handles an edge case where line x and line x+1 are equal
                # and are the last two lines in the puzzle
                return line_id
            for r_id in range(1, compare_offset+1):
                if not check_row_entries(puzzle, line_id-r_id, line_id+r_id+1):
                    # This would break this line and check the next one
                    break
                elif r_id == (compare_offset) and check_row_entries(puzzle, line_id-r_id, line_id+r_id+1):
                    # If all offset lines match then return
                    return line_id


def find_col_ref_line(puzzle, start):
    for col_id in range(len(puzzle[0])):
        if col_id <= start:
            continue
        num_left = col_id
        num_right = len(puzzle[0])-1-col_id
        compare_offset = min(num_left, num_right)
        if compare_offset == 0:
            if num_right > 0 and check_col_entries(puzzle, col_id, col_id+1):
                return col_id
            else:
                continue

        if check_col_entries(puzzle, col_id, col_id+1):
            compare_offset = min(num_left, (num_right-1))
            if compare_offset == 0:
                # This handles an edge case where line x and line x+1 are equal
                # and are the last two lines in the puzzle
                return col_id
            for c_id in range(1, compare_offset+1):
                if not check_col_entries(puzzle, col_id-c_id, col_id+c_id+1):
                    # This would break this line and check the next one
                    break
                elif c_id == (compare_offset) and check_col_entries(puzzle, col_id-c_id, col_id+c_id+1):
                    # If all offset lines match then return
                    return col_id


def day_13(path, part_one=False):
    answer = 0
    data = []
    with open(path, "r") as f:
        # for line in f.readlines():
        #     l, r = line.strip().split()
        lines = f.read().splitlines()
        # data = f.read().split("")a
        for i, line in enumerate(lines):
            if i == 0 or line == "":
                data.append([])

            if line == "":
                continue

            data[-1].append(list(line))

    for p_id, puzzle in enumerate(data):
        if p_id == 49:
            pass
        col_id = find_col_ref_line(puzzle, -5)
        # print(f'puzzle: {p_id} col: {col_id}')
        while col_id is not None:
            if (col_id+1):
                answer += col_id+1
            # print(f'puzzle: {p_id} col: {col_id} start: {col_id}')
            col_id = find_col_ref_line(puzzle, col_id)

        row_id = find_horizontal_reflection_line(puzzle, -5)
        # print(f'puzzle: {p_id} row_id: {row_id}')
        while row_id is not None:
            if (row_id+1):
                answer += (100*(row_id+1))
            # print(f'puzzle: {p_id} row_id: {row_id} start: {row_id}')
            row_id = find_horizontal_reflection_line(
                puzzle, row_id)

    return answer


start_time = time.time()
# print(day_13("./inputs/day_13_sample.txt", part_one=True))
# part 1: 43614
print(day_13("./inputs/day_13_input.txt", part_one=True))
print("--- %s seconds ---" % (time.time() - start_time))
