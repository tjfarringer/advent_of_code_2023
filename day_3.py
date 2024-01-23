from collections import defaultdict
import sys
import math as m
import re
import utilities


def day_three(path):
    gears = defaultdict(list)
    part_numbers = []
    # Read the entire txt file into memory
    with open(path) as f:
        data = f.readlines()

    # data = ["467..114..",
    #         "/..*......",
    #         "..35..633.",
    #         "......#...",
    #         "617*......",
    #         ".....+.58.",
    #         "..592.....",
    #         "......755.",
    #         "...$.*.*..",
    #         ".664.598./"]

    # data = ["349...*.............402...735......@................182.121...134........%255.276...%...&.../............460....#......79...................",
    #         "....503....22.............#.....$............38.....+...........*....-11.......*......326...../....*853.........216......*.../180.....16...."]

    for line_idx, line in enumerate(data):
        first_number_indx_rng = 0
        search_range = 0
        while not first_number_indx_rng is None:
            # Steps:
            # 1 -- check line for first number
            # print(f'test serach rng: {search_range}. {len(data[0])}')
            first_number_indx_rng = utilities.find_first_int(line[search_range: len(data[0])], reversed=False, letters_as_words=False,
                                                             find_entire_number=True, indices_rather_than_number=True)
            # print(f'checking: {first_number_indx_rng}')
            # If no more numbers then move onto the next line
            if first_number_indx_rng is None:
                continue

            # Need to update the number-indx-range
            # because that fncn is retruning values as of the edited line
            # adding 1 to the end range index because we want to search upto and including that last digit
            updated_indx = (
                first_number_indx_rng[0]+search_range, first_number_indx_rng[1]+search_range+1)

            # 2 -- check if that number is surrounded by a symbol
            surrounded = utilities.surrounded_by_symbol(
                data, line_idx, updated_indx, gears)
            # 3 -- if so, store, otherwise move onto the next number
            if surrounded:
                # print(
                #     f'value: {data[line_idx][updated_indx[0]:updated_indx[1]]}')
                part_numbers.append(
                    int(data[line_idx][updated_indx[0]:updated_indx[1]]))

            search_range = updated_indx[1]+1

    # print(part_numbers)
    # Removing duplicates did not give the correct results..
    # part_numbers = list(set(part_numbers))
    return sum(part_numbers)


# print(day_three("day_3_input.txt"))
# 522985 --


gears = defaultdict(list)
gears[(3, 2)].append((2, 3))
gears[(3, 2)].append((5, 8))
print(gears)
