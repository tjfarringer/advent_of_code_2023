import time

# . => empty space
# # => galaxy

# goal:  sum of the lengths of the shortest path between every pair of galaxies
# Can only move 1 square at a time (up, down, left, right)

# any row or column w/o a galaxy should be doubled
# ie. 1 empty row should turn into 2 empty rows


def check_empty_row(row):
    for entry_idx, entry in enumerate(row):
        if entry == "#":
            # Break and check the next line
            return False
    return True


def check_empty_col(grid, col_idx):
    for row in grid:
        if row[col_idx] == "#":
            return False
    return True


def manhattan_distance(node_1, node_2, duplicate_rows, duplicate_cols, part_one):
    add_row_col = 1 if part_one else 999999

    min_line = node_1[0] if node_1[0] < node_2[0] else node_2[0]
    max_line = node_1[0] if node_1[0] >= node_2[0] else node_2[0]
    min_entry = node_1[1] if node_1[1] < node_2[1] else node_2[1]
    max_entry = node_1[1] if node_1[1] >= node_2[1] else node_2[1]

    distance = abs(node_2[1]-node_1[1]) + abs(node_2[0]-node_1[0])
    # now check if we hit an empty row
    for row_i in range(min_line, max_line+1):
        if row_i in duplicate_rows:
            distance += add_row_col
    for col_i in range(min_entry, max_entry+1):
        if col_i in duplicate_cols:
            distance += add_row_col

    return distance


def day_11(path, part_one=False):
    # Rather than expand the grid for the additional rows/cols
    # I added those values in when calculating the manhattan distance
    row_idx_insertion = []
    col_idx_insertion = []
    shortest_distances = []
    all_nodes = []
    with open(path, "r") as f:
        grid = [list(l.strip()) for l in f]

    # Check for an empty row and append it to the list
    start_time = time.time()

    for row_idx, row in enumerate(grid):
        if check_empty_row(row):
            # if we hit here then it was an empty line
            row_idx_insertion.append(row_idx)
    # Check for an empty col and append it to the list
    for col_idx in range(0, len(grid[0])):
        if check_empty_col(grid, col_idx):
            # if we hit here then it was an empty line
            # row_idx_insertion.append(row_idx)
            col_idx_insertion.append(col_idx)
    print("to find empty rows/cols --- %s seconds ---" %
          (time.time() - start_time))

    # Find all the nodes
    start_time = time.time()

    for l_id, line in enumerate(grid):
        for e_id, entry in enumerate(row):
            if grid[l_id][e_id] == "#":
                all_nodes.append((l_id, e_id))
    print("to find all nodes --- %s seconds ---" % (time.time() - start_time))

    # Can use manhattan distance between the two nodes
    start_time = time.time()
    while len(all_nodes) > 0:
        node_1 = all_nodes.pop()
        for node_2 in all_nodes:
            distance = manhattan_distance(
                node_1, node_2, duplicate_rows=row_idx_insertion, duplicate_cols=col_idx_insertion, part_one=part_one)
            # visited_nodes.append(node_1)
            shortest_distances.append(distance)
    print("to find distance --- %s seconds ---" % (time.time() - start_time))

    return sum(shortest_distances)


start_time = time.time()
# part1: 9312968 -- 170 seconds
# part1:  removing from the all_nodes list turns this down to 0.03 seconds
# part2: 597714117556
print(day_11("day_11_input.txt"))
print("--- %s seconds ---" % (time.time() - start_time))
