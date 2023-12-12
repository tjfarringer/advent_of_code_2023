import functools
# which springs are safe?  Also the record is damaged

# rows = springs
# "." => operational "#" => damaged "?" => unknown
# after this there are numbers which indicate how many damaged springs are in a row

# Goal:  How many different arrangements of operational and broken springs fit the given criteria in each row?


@functools.cache
def num_matches(line, size, dmg_size):
    count = 0

    if len(dmg_size) == 0:
        if all(c in '.?' for c in line):
            return 1
        return 0

    a = dmg_size[0]
    rest = dmg_size[1:]
    # Add len(rest) because you always need at least 1 . between entries
    # sum(rest) because you need that many characters
    after = sum(rest) + len(rest)

    # Looping through all the spots a could potentially go into
    for before in range(size-after-a+1):
        cand = '.' * before + '#' * a + '.'
        # Making sure this position is actually valid
        if all(c0 == c1 or c0 == '?'
               for c0, c1 in zip(line, cand)):
            # If valid for the first position then go onto the remaining ones
            count += num_matches(line[len(cand):],
                                 size-a-before-1,
                                 rest)

    return count


def day_12(path, copies=1):
    combinations = 0
    with open(path, "r") as f:
        for line in f.readlines():
            l, r = line.strip().split()
            line_pattern = '?'.join((l,) * copies)
            dmg_size = tuple(map(int, r.split(','))) * copies
            combinations += num_matches(line_pattern,
                                        len(line_pattern), dmg_size)

    return combinations


# print(day_12("./inputs/day_12_sample.txt", copies=1))
print(day_12("./inputs/day_12_input.txt", copies=5))
