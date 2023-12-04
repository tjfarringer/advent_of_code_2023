import time
import utilities
from collections import defaultdict
# Scratchpads
# winning numbers | numbers you have

# which numbers you have appear in the list of winning numbers?
# First match = 1 point.  Every other match = total-pts * 2


# Part 2:
# Winning number of a card will give you copies of the x following cards
# ex:  winning number = 2 will give you copies of cards {i+1, i+2}
# How many total cards do we end up with?
# WILL NOT get a copy of a card past the end of the table

def day_four(path, part_one=False):
    card_values = []
    # Note:  need to put "int" in for defaultdict so the values know to default to 0
    scorecard_copies = defaultdict(int)
    match_count = {}

    # Read the entire txt file into memory
    with open(path, "r") as f:
        # splitlines allows us to remove those "/n" values
        data = f.read().splitlines()

    final_card = utilities.find_first_int(data[len(data)-1], reversed=False,
                                          letters_as_words=False, find_entire_number=True, indices_rather_than_number=False)

    for line_idx, line in enumerate(data):
        card_number = utilities.find_first_int(line, reversed=False,
                                               letters_as_words=False, find_entire_number=True, indices_rather_than_number=False)
        card_value = 0
        num_matching = 0
        # update copy count for the exisiting card
        scorecard_copies[card_number] += 1

        # print(line)
        line = line.replace("  ", " ")
        # remove card x: value
        line = line.split(":")[1]
        winning_numbers = filter(None, line.split("|")[0].split(" "))
        winning_numbers = list(winning_numbers)

        our_numbers = filter(None, line.split("|")[1].split(" "))
        our_numbers = list(our_numbers)

        if (match_count.get(card_number, -1) != -1):
            num_matching = match_count.get(card_number, -1)
        else:
            for number in our_numbers:
                if number in winning_numbers:
                    if card_value == 0:
                        card_value = 1
                    else:
                        card_value *= 2
                    # increment num_matching -- this is for part 2
                    num_matching += 1
            card_values.append(int(card_value))
            match_count[card_number] = num_matching

        if not part_one:
            for x in range(1, num_matching+1):
                # Add the copy back to data so we process the copy
                if (x+card_number) <= final_card:
                    data.append(data[x+card_number-1])

    if part_one:
        return sum(card_values)
    else:
        return sum(scorecard_copies.values())


# print(day_four("day_4_sample.txt", part_one=False))
start_time = time.time()
print(day_four("day_4_input.txt", part_one=False))
print("--- %s seconds ---" % (time.time() - start_time))
# 93 seconds w/o the num-matching cache -- answer: 10378710
# 45 seconds w/ the num-matching cache -- answer: 10378710
