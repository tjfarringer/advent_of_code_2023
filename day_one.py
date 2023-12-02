import utilities
# Elves gave us a map
# stars indicate top fifty locations that have problems
# Need to check all 50-stars by Dec-25

# On each line, the calibration value can be found by combining
# the first digit and the last digit (in that order) to form a single two-digit number.


def puzzle_one(path="puzzle_one_input.txt"):
    digit_list = []

    # Read in the input file
    content = utilities.read_txt_file(path)

    # Find first and last digit in the string
    # Append to digit list
    for line in content:
        first_digit = utilities.find_first_int(
            line, reversed=False, letters_as_words=True)
        last_digit = utilities.find_first_int(
            line[::-1], reversed=True, letters_as_words=True)

        final_val = first_digit + last_digit
        digit_list.append(int(final_val))

    return sum(digit_list)


print(puzzle_one())
# 54530
