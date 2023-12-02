import utilities
import re

# Play a game with the elf

# bag w/ some cubes -- Red, Green, or Blue
# will hide secret num of cubes of each color in the bag
# goal: figure out info about the number of cubes

# Elf will show us a few samples from the bag

# Which games would have been possible if the bag contained only 12 red, 13 green, and 14 blue

# What is the sum of games that would have been possibe?

constraints_dict = {'green': 13, 'red': 12, 'blue': 14}

# part two:
# what is the max num of cubes per game?
# Find the power by multiplying the max num of cubes for each type
# Then sum across games


def day_two(path):
    # possible_games = []
    cube_power = []

    with open(path) as file:
        for idx, game in enumerate(file):

            max_red = 0
            max_green = 0
            max_blue = 0

            # content = ["Game 1: 3 blue, 7 green, 10 red; 4 green, 4 red; 1 green, 7 blue, 5 red; 8 blue, 10 red; 7 blue, 19 red, 1 green",
            #            "Game 2: 6 red, 10 green; 11 green, 4 red; 16 green, 2 blue; 7 green, 5 blue, 4 red; 17 green, 1 red, 1 blue"]

            # for idx, game in enumerate(content):
            # for sample in game.split(';'):
            val_to_append = int(idx+1)
            for sample in filter(None, re.split("[,;:]+", game)):
                for key in constraints_dict.keys():
                    if key in sample.lower():
                        # relevant_constraint = constraints_dict.get(key)
                        num_balls = utilities.find_first_int(sample, reversed=False, letters_as_words=False,
                                                             find_entire_number=True)
                        # if int(num_balls) > relevant_constraint:
                        #     val_to_append = 0
                        if key == 'green' and num_balls > max_green:
                            max_green = num_balls
                        elif key == 'red' and num_balls > max_red:
                            max_red = num_balls
                        elif key == 'blue' and num_balls > max_blue:
                            max_blue = num_balls

            cube_power.append(max_green*max_red*max_blue)
            # possible_games.append(val_to_append)
            # print(possible_games)
        return sum(cube_power)


print(day_two(path="puzzle_2_input.txt"))
# print(utilities.find_first_number("10 red"))
