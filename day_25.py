import networkx as nx
from networkx.algorithms.flow import minimum_cut
import random
import time
# Can only disconnect 3 wires
# name of a component, a colon,
# then a list of other components to which that component is connected

# Each connection between two components is represented only once
# Connections are not directional

# Goal:
# Find the three wires you need to disconnect in order to divide the components into two separate groups.
# What do you get if you multiply the sizes of these two groups together?

# Algo to use is the min-cut algorithm


def day_25(path, part_two=False):
    G = nx.Graph()
    # G.add_edge("x", "a", capacity=3.0)
    # Creating our data structures
    with open(path, "r") as f:
        for line in f.readlines():
            start_pt, conns = line.split(":")
            conns = conns.rstrip()
            conns = conns.split(" ")
            valid_conns = [x for x in conns if x]

            for c in valid_conns:
                G.add_edge(start_pt, c, capacity=1.0)

    all_nodes = list(G.nodes)
    min_cut = -1
    while min_cut != 3:
        min_cut, partition = nx.minimum_cut(
            G, random.choice(all_nodes), random.choice(all_nodes))

    print(f'Part 1 val: {len(partition[0])*len(partition[1])}')


start_time = time.time()

# day_25("./inputs/day_25_sample.txt")
day_25("./inputs/day_25_input.txt")
print("--- %s seconds ---" % (time.time() - start_time))
