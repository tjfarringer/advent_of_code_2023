from collections import defaultdict
# string => single num in range(0,255)
# start w/ curr val of 0
# then for each char:
# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.

# part 2:
# dash => go to relevant box and remove lens with the given label (if present)
# Then move all other lenses as far forward in the box as they can go w/o changing order
# equals => focal len
# If lens already in the box then replace the old lens w/ the new one
# If not already a lens add the lens to the box imm. behind any lenses

box_dict = defaultdict(list)


def custom_hash(string, part_two=False, label=False):
    current_value = 0
    label_val = ""

    for character in string:
        if part_two:
            if character in ["=", "-"]:
                break
        ascii = ord(character)
        current_value += ascii
        current_value *= 17
        current_value = current_value % 256
        label_val += character

    if label:
        return label_val
    return current_value


def focal_power(box_dict):
    answer = 0
    # multiply together
    # 1 + box number
    # slot of the lens (first = 1, 2 = second, etc)
    # focal len
    for box_num in box_dict.keys():
        for slot_num, lens in enumerate(box_dict[box_num]):
            focal_power = 1
            focal_power *= (box_num+1)
            focal_power *= (slot_num+1)
            focal_power *= int(lens[-1])
            answer += focal_power

    return answer


def day_15(path, part_two=False):
    part_one_answer = 0
    # be sure to ignore newline characters
    with open(path, "r") as f:
        entry_values = [line.strip().rstrip('\r\n').split(',') for line in f]

    for string in entry_values[0]:
        part_one_answer += custom_hash(string, part_two=False)
    print(f'part 1 answer: {part_one_answer}')

    if part_two:
        for string in entry_values[0]:
            box = custom_hash(string, part_two)
            label = custom_hash(string, part_two, label=True)

            if "=" in string:
                focal_len = string[-1]
                entry = ""
                entry += (label + " " + focal_len)

                if len(list(filter(lambda x: x.startswith(label), box_dict[box]))) > 0:
                    box_dict[box][:] = [
                        entry if x.startswith(label) else x for x in box_dict[box]]
                else:
                    # add new label
                    box_dict[box].append(entry)
            elif "-" in string:
                if len(list(filter(lambda x: x.startswith(label), box_dict[box]))) > 0:
                    result = list(
                        filter(lambda x: x.startswith(label), box_dict[box]))
                    for x in result:
                        box_dict[box].remove(x)

        print(f'part 2 answer: {focal_power(box_dict)}')


day_15("./inputs/day_15_input.txt", part_two=True)
