
# Each line is a history of a single value
# Want to make a prediction of the next value
# Steps:
# 1 -- make new sequences from the difference at each step in the history
# If not all 0's then repeat this process using the new sequence as the input
# Once all values are zeros you can extrapolate what the next val should be

# Goal:  sum all the extrapolated values

def take_difference(sequence):
    new_seqeuence = []
    for idx in range(1, len(sequence)):
        diff = sequence[idx] - sequence[idx-1]
        new_seqeuence.append(diff)
    return new_seqeuence


def day_9(path, part_one=False):
    extrapolated_values = []
    with open(path, "r") as f:
        lines = [line.strip().split(" ") for line in f.readlines()]

    for line in lines:
        # Convert the list to integers
        line = [int(x) for x in line]
        current_sequence = line
        # setup list to capture each element needed to find the extrapolated val
        diff_list = []

        if part_one:
            # part one is forecasting forward
            diff_list.append(current_sequence[len(current_sequence)-1])
            while sum(current_sequence) != 0:
                current_sequence = take_difference(current_sequence)
                diff_list.append(current_sequence[len(current_sequence)-1])
            extrapolated_values.append(sum(diff_list))
        else:
            # part two is forecasting backwards
            diff_list.append(current_sequence[0])
            running_sum = 0

            # Build list of differences in the sequences
            while sum(current_sequence) != 0:
                current_sequence = take_difference(current_sequence)
                diff_list.append(current_sequence[0])

            # Take running sum to find the extrapolated value
            for idx in range(len(diff_list)-2, -1, -1):
                running_sum = diff_list[idx] - running_sum
            extrapolated_values.append(running_sum)

    return sum(extrapolated_values)


# part1: 1637452029
# part2: 908
print(day_9("day_9_input.txt", part_one=True))
