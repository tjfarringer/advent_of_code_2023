
int_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def read_txt_file(path):
    file = open(path, "r")
    return file.readlines()


def find_first_int(line, reversed=False, letters_as_words=False, find_entire_number=False):
    for indx, char in enumerate(line):
        # If the char is a number then return it
        if char.isdigit():
            # One problem wants the entire digit rather than just the first int
            # This path captures that
            if find_entire_number:
                number = ""
                number += str(char)
                for x in range(indx+1, len(line)):
                    if line[x].isdigit():
                        number += str(line[x])
                    else:
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
