# Elves gave us a map
# stars indicate top fifty locations that have problems
# Need to check all 50-stars by Dec-25

# On each line, the calibration value can be found by combining
# the first digit and the last digit (in that order) to form a single two-digit number.

# key, len(key)
int_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def find_first_int(line, reversed=False):
    for indx, char in enumerate(line):
        # If the char is a number then return it
        if char.isdigit():
            return char

        # Now check if the value is a word
        for key in int_dict.keys():
            orig_key = key
            if reversed:
                key = key[::-1]

            if char == key[0]:
                if line[indx:len(key)+indx] == key:
                    return int_dict[orig_key]


def puzzle_one(path="puzzle_one_input.txt"):
    digit_list = []

    # Read in the input file
    file = open(path, "r")
    content = file.readlines()

    # Find first and last digit in the string
    # Append to digit list
    for line in content:
        first_digit = find_first_int(line)
        last_digit = find_first_int(line[::-1], reversed=True)

        final_val = first_digit + last_digit
        digit_list.append(int(final_val))

    return sum(digit_list)


print(puzzle_one())
