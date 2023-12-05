import time

# shows seeds that need to be planted
# inputs:  soil, water, etc
# each category reuses the numbers

# First line:  indicates which seeds need to be planted

# Maps correspond to ranges of numbers
# Each line within a map contains three numbers:
# the destination range start, the source range start, and the range length.

# If the mapping doesn't exist then the source = dest

# Goal:
# find lowest location number that corresponds to any of the initial seeds


def build_map(line, map):
    line_broken = line.split(' ')
    # source-begin, dest-begin, source-end
    insertion_key = (int(line_broken[1]), int(
        line_broken[0]), int(line_broken[2])+int(line_broken[1])-1)
    map.append(insertion_key)
    return map


def map_lookup(value, map):
    for source_begin, dest_begin, source_end in map:
        if source_begin <= value < source_end:
            return dest_begin + (value - source_begin)

    return value


def find_location(seed, seed_to_soil_map, soil_to_fert_map, fert_to_water_map, water_to_light_map, light_to_temp_map, temp_to_hum_map, hum_to_location_map):
    soil_value = map_lookup(seed, seed_to_soil_map)
    fert_value = map_lookup(soil_value, soil_to_fert_map)
    water_value = map_lookup(fert_value, fert_to_water_map)
    light_value = map_lookup(water_value, water_to_light_map)
    temp_value = map_lookup(light_value, light_to_temp_map)
    hum_value = map_lookup(temp_value, temp_to_hum_map)
    location_value = map_lookup(hum_value, hum_to_location_map)
    return location_value


def day_five(path, part_one=False, testing=False):
    seeds = [1636419363, 608824189, 3409451394, 227471750, 12950548, 91466703, 1003260108, 224873703,
             440703838, 191248477, 634347552, 275264505, 3673953799, 67839674, 2442763622, 237071609, 3766524590, 426344831, 1433781343, 153722422]
    seed_to_soil_map = []
    soil_to_fert_map = []
    fert_to_water_map = []
    water_to_light_map = []
    light_to_temp_map = []
    temp_to_hum_map = []
    hum_to_location_map = []
    seed_locations = []
    # Read the entire txt file into memory
    with open(path, "r") as f:
        # splitlines allows us to remove those "/n" values
        data = f.read().splitlines()

    for line_idx, line in enumerate(data):
        if line_idx >= 3 and line_idx <= 31:
            seed_to_soil_map = build_map(line, seed_to_soil_map)
        elif line_idx >= 34 and line_idx <= 52:
            # print(f'{line}')
            soil_to_fert_map = build_map(line, soil_to_fert_map)
        elif line_idx >= 55 and line_idx <= 96:
            # print(f'{line}')
            fert_to_water_map = build_map(line, fert_to_water_map)
        elif line_idx >= 99 and line_idx <= 116:
            # print(f'{line}')
            water_to_light_map = build_map(line, water_to_light_map)
        elif line_idx >= 119 and line_idx <= 131:
            # print(f'{line}')
            light_to_temp_map = build_map(line, light_to_temp_map)
        elif line_idx >= 134 and line_idx <= 143:
            # print(f'{line}')
            temp_to_hum_map = build_map(line, temp_to_hum_map)
        elif line_idx >= 146 and line_idx <= 189:
            # print(f'{line}')
            hum_to_location_map = build_map(line, hum_to_location_map)

    # todo: sort the maps
    seed_to_soil_map = sorted(seed_to_soil_map, key=lambda x: x[0])
    soil_to_fert_map = sorted(soil_to_fert_map, key=lambda x: x[0])
    fert_to_water_map = sorted(fert_to_water_map, key=lambda x: x[0])
    water_to_light_map = sorted(water_to_light_map, key=lambda x: x[0])
    light_to_temp_map = sorted(light_to_temp_map, key=lambda x: x[0])
    temp_to_hum_map = sorted(temp_to_hum_map, key=lambda x: x[0])
    hum_to_location_map = sorted(hum_to_location_map, key=lambda x: x[0])

    if testing:
        seeds = [79, 14, 55, 13]
        # seeds = [14]
        seed_to_soil_map = [(50, 52, 98),
                            (98, 50, 100)]
        soil_to_fert_map = [(15, 0, 52),
                            (52, 37, 54),
                            (0, 39, 15)]
        fert_to_water_map = [(53, 49, 61), (11, 0, 53),
                             (0, 42, 7), (7, 57, 11)]
        water_to_light_map = [(18, 88, 25), (25, 18, 95)]
        light_to_temp_map = [(77, 45, 100), (45, 81, 64), (64, 68, 77)]
        temp_to_hum_map = [(69, 0, 70), (0, 1, 69)]
        hum_to_location_map = [(56, 60, 93), (93, 56, 97)]

        # for map_list in (seed_to_soil_map, soil_to_fert_map, fert_to_water_map, water_to_light_map, light_to_temp_map, temp_to_hum_map, hum_to_location_map):
        seed_to_soil_map = sorted(seed_to_soil_map, key=lambda x: x[0])
        soil_to_fert_map = sorted(soil_to_fert_map, key=lambda x: x[0])
        fert_to_water_map = sorted(fert_to_water_map, key=lambda x: x[0])
        water_to_light_map = sorted(water_to_light_map, key=lambda x: x[0])
        light_to_temp_map = sorted(light_to_temp_map, key=lambda x: x[0])
        temp_to_hum_map = sorted(temp_to_hum_map, key=lambda x: x[0])
        hum_to_location_map = sorted(hum_to_location_map, key=lambda x: x[0])

    if part_one:
        for seed in seeds:
            seed_location = find_location(seed, seed_to_soil_map, soil_to_fert_map, fert_to_water_map,
                                          water_to_light_map, light_to_temp_map, temp_to_hum_map, hum_to_location_map)
            seed_locations.append(seed_location)
        return min(seed_locations)
    else:
        for idx, x in enumerate(seeds[::2]):
            for seed in range(x, seeds[(idx*2)+1]+x):
                seed_location = find_location(seed, seed_to_soil_map, soil_to_fert_map, fert_to_water_map,
                                              water_to_light_map, light_to_temp_map, temp_to_hum_map, hum_to_location_map)
                seed_locations.append(seed_location)
        return min(seed_locations)


start_time = time.time()
print(day_five("day_5_input.txt", part_one=True, testing=False))
print("--- %s seconds ---" % (time.time() - start_time))
# print(day_five("day_5_input.txt", testing=True))
