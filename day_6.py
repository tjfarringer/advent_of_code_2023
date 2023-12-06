import time
import math

# time allowed for each race
# best distance ever recorded for that race
# You get x time and want to travel as far as you can

# Need to go farther in each race than the current record holder
# holding down the button charges the boat.  Releasing allows it to move.
# Time spent holding the button counts against the race time.  But the longer you hold it the faster it goes.

# Each ms holding down, the boat's speed increases by 1 millimeter per second
# Goal: num ways you can beat the record in each race.  Multiply them together and return.


def day_six_part_one(path, testing=False):
    num_ways_to_win_per_race = []
    with open(path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        time_line, dist_line = [line_nums.split() for line_nums in [
            line.split(":")[1].strip() for line in lines]]
        time_line = [int(num) for num in time_line]
        dist_line = [int(num) for num in dist_line]
        puzzle_input = list(zip(time_line, dist_line))

    if testing:
        puzzle_input = [(7, 9), (15, 40), (30, 200)]

    for race in puzzle_input:
        num_ways_to_win = 0
        for ts in range(1, race[0]+1):
            distance = ts * (race[0]-ts)
            if distance > race[1]:
                num_ways_to_win += 1
        num_ways_to_win_per_race.append(num_ways_to_win)
    return math.prod(num_ways_to_win_per_race)


def day_six_part_two(path, testing=False):
    first_ts_past_record = last_ts_past_record = 0

    with open(path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        time_line, dist_line = [line_nums.split() for line_nums in [
            line.split(":")[1].strip() for line in lines]]
        time_line = int("".join(time_line))
        dist_line = int("".join(dist_line))
        puzzle_input = [(time_line, dist_line)]

    if testing:
        puzzle_input = [(71530, 940200)]

    # Brute force approach
    # for race in puzzle_input:
    #     for ts in range(1, race[0]+1):
    #         distance = ts * (race[0]-ts)
    #         if distance > race[1]:
    #             num_ways_to_win += 1

    # More optimized way -- find first/last number past record and subtract
    for race in puzzle_input:
        for ts in range(1, race[0]+1):
            distance = ts * (race[0]-ts)
            if distance > race[1]:
                first_ts_past_record = ts
                break

    for race in puzzle_input:
        for ts in reversed(range(1, race[0]+1)):
            distance = ts * (race[0]-ts)
            if distance > race[1]:
                last_ts_past_record = ts
                break

    return (last_ts_past_record - first_ts_past_record + 1)


start_time = time.time()
# print(day_six_part_one("day_6_input.txt", testing=False))
# part1 answer: 608902
print(day_six_part_two("day_6_input.txt", testing=False))
# part2 answer: 46173809 -- brute force takes 5 seconds
# part2 answer: 46173809 -- better approach takes 0.8 seconds
print("--- %s seconds ---" % (time.time() - start_time))
