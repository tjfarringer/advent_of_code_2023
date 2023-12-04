# Scratchpads
# winning numbers | numbers you have

# which numbers you have appear in the list of winning numbers?
# First match = 1 point.  Every other match = total-pts * 2

def day_four(path):
    card_values = []
    # Read the entire txt file into memory
    with open(path, "r") as f:
        # splitlines allows us to remove those "/n" values
        data = f.read().splitlines()

    for line_idx, line in enumerate(data):
        card_value = 0

        # print(line)
        line = line.replace("  ", " ")
        # remove card x: value
        line = line.split(":")[1]
        winning_numbers = filter(None, line.split("|")[0].split(" "))
        winning_numbers = list(winning_numbers)

        our_numbers = filter(None, line.split("|")[1].split(" "))
        our_numbers = list(our_numbers)

        for number in our_numbers:
            if number in winning_numbers:
                if card_value == 0:
                    card_value = 1
                else:
                    card_value *= 2
        card_values.append(int(card_value))

    return sum(card_values)


print(day_four("day_4_input.txt"))
