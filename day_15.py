
# string => single num in range(0,255)
# start w/ curr val of 0
# then for each char:
# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.

def custom_hash(string):
    current_value = 0

    for character in string:
        ascii = ord(character)
        current_value += ascii
        current_value *= 17
        current_value = current_value % 256

    return current_value


def day_15(path):
    answer = 0
    # be sure to ignore newline characters
    with open(path, "r") as f:
        list = [line.strip().rstrip('\r\n').split(',') for line in f]

    for string in list[0]:
        # print(f'string: {string}')
        answer += custom_hash(string)

    return answer


print(day_15("./inputs/day_15_input.txt"))
