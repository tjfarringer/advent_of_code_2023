from collections import Counter
import numpy as np
# Camel Cards
# Input:  list of hands
# Want to order them based on the strength of each hand
# Hand contains 5 cards (A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2)

# 7 different 'hands'

# If a tie:
# second ordering rule:
# compare the first card in each hand.  If diff then the highest card wins

# Total winnings = bid * (rank of the hand) -- best hand has n rank where n = num-hands.  Lowest hand has rank of 1
# Find sum of total-winnings of all the hands

# Steps?
# 1 find each hand's type
# 2 sort within each type (maybe convert each card to a number and then sort desc)
# 3 convert to rank
# 4 sum up the winnings


def find_hand_type(hand, part_one=False):
    char_count = Counter(hand)
    most_common_count = char_count.most_common(1)[0][1]
    # if there is a joker add it to the most common card
    if not part_one and 'J' in char_count and len(char_count) > 1:
        most_common_count = char_count.pop(
            'J', 0) + char_count.most_common(1)[0][1]
    num_unique_chars = len(char_count)
    match most_common_count:
        case 5:
            # five of a kind
            return '8'
        case 4:
            # four of a kind
            return '7'
        case 3:
            # full-house or 3 of a kind
            return '6' if num_unique_chars == 2 else '5'
        case 2:
            # two-pair or 1-pair
            return '4' if num_unique_chars == 3 else '3'
        case _:
            # high-card
            return '2'


def convert_hand_to_nums(hand, part_one):
    hand_sum = 0
    if part_one:
        digits = '23456789TJQKA'
    else:
        # move joker to be the lowest ranked card for the tie breaker
        digits = 'J23456789TQKA'

    for idx, card in enumerate(hand[::-1]):
        hand_sum += digits.index(card) * (14 ** idx)

    # print(f'hand: {hand}. sum: {hand_sum}')
    return hand_sum


def day_seven(path, testing=False, part_one=False):
    total_winnings = 0
    hand_types = []
    with open(path, "r") as f:
        hands, bids = zip(*[(handstr, int(bidstr)) for handstr,
                          bidstr in map(lambda line: line.strip().split(), f.readlines())])
        for hand in range(0, len(hands)):
            hand_type = find_hand_type(hands[hand])
            hand_type_combined = convert_hand_to_nums(
                hand_type + hands[hand], part_one)
            hand_types.append(hand_type_combined)

        _, bids_sorted = zip(
            *sorted(zip(hand_types, bids), key=lambda x: x[0]))

        for x in range(0, len(hand_types)):
            total_winnings += (x+1)*bids_sorted[x]

    return total_winnings


print(day_seven("day_7_input.txt", part_one=False))
