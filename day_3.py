import utilities


def day_three(path):
    part_numbers = []
    # Read the entire txt file into memory
    with open(path) as f:
        data = f.readlines()

    data = ["48.................501....33.....622..............763.........331.................161.683......................................980..........",
            "...491.842.....948*..................338.....*......=...........-...309.......633*....*....................*990...706...452......*..+......."]

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
            # first_number_indx_rng[0] = first_number_indx_rng[0] + search_range
            # first_number_indx_rng[1] += search_range

            updated_indx = (
                first_number_indx_rng[0]+search_range, first_number_indx_rng[1]+search_range+1)

            # 2 -- check if that number is surrounded by a symbol
            surrounded = utilities.surrounded_by_symbol(
                data, line_idx, updated_indx)
            # 3 -- if so, store, otherwise move onto the next number
            if surrounded:
                # print(
                #     f'value: {data[line_idx][updated_indx[0]:updated_indx[1]]}')
                part_numbers.append(
                    int(data[line_idx][updated_indx[0]:updated_indx[1]]))

            search_range = updated_indx[1]+1

    print(part_numbers)
    return sum(part_numbers)


print(day_three("day_3_input.txt"))
# tuple_returned = utilities.find_first_int("Hel123lo", reversed=False, letters_as_words=False,
#                                           find_entire_number=True, indices_rather_than_number=True)

# print(tuple_returned)
# print(tuple_returned[1])
# find_first_int(line, reversed=False, letters_as_words=False, find_entire_number=False, indices_rather_than_number=False):

# data = ["48.................501....33.....622..............763.........331.................161.683......................................980..........",
#         "...491.842.....948*..................338.....*......=...........-...309.......633*....*....................*990...706...452......*..+......."]

# # print(data[17:20])
# print(len(data[0]))
