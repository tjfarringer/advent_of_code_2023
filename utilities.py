
int_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def read_txt_file(path):
    file = open(path, "r")
    return file.readlines()


def find_first_int(line, reversed=False, letters_as_words=False, find_entire_number=False, indices_rather_than_number=False):
    for indx, char in enumerate(line):
        # If the char is a number then return it
        if char.isdigit():
            # One problem wants the entire digit rather than just the first int
            # This path captures that
            if find_entire_number:
                start_idx = indx
                number = ""
                number += str(char)
                for x in range(indx+1, len(line)):
                    if line[x].isdigit():
                        number += str(line[x])
                    else:
                        if indices_rather_than_number:
                            end_indx = x - 1
                            return (start_idx, end_indx)

                        return int(number)
            # This path gives us the first int
            else:
                return char

        # Now check if the value is a word
        if letters_as_words:
            for key in int_dict.keys():
                orig_key = key
                if reversed:
                    key = key[::-1]

                if char == key[0]:
                    if line[indx:len(key)+indx] == key:
                        return int_dict[orig_key]


def is_symbol(value):
    special_characters = '"!@#$%^&*()-+?_=,<>/"'
    if any(c in special_characters for c in value):
        return True
    return False


def check_neighbors(data, line_number, entry_nbr):
    if line_number - 1 >= 0:
        # todo add boundary checks here
        for x in range(entry_nbr-1, entry_nbr+1):
            if x >= 0 and x < len(data[0]):
                if is_symbol(data[line_number-1][x]):
                    return True
    if entry_nbr-1 >= 0:
        if is_symbol(data[line_number][entry_nbr-1]):
            return True
    if entry_nbr+1 < len(data[0]):
        if is_symbol(data[line_number][entry_nbr+1]):
            return True
    if line_number + 1 < len(data[0]):
        for x in range(entry_nbr-1, entry_nbr+1):
            if x >= 0 and x < len(data[0]):
                if is_symbol(data[line_number+1][x]):
                    return True

    return False


def surrounded_by_symbol(data, line_number, entry_rng):
    # for each number in the range
    # does it's immediate neighbors include a symbol?
    # If so, return True
    for entry in range(entry_rng[0], entry_rng[1]+1):
        if check_neighbors(data, line_number, entry):
            return True

    return False
