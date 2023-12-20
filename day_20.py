import time
from queue import Queue
# High or low pulse

# Flip-flop modules (prefix %) are either on or off
# Initially off
# if a flip-flop module receives a low pulse, it flips between on and off. If it was off,
# it turns on and sends a high pulse.
# If it was on, it turns off and sends a low pulse.

# Conjunction modules (prefix &)
# These remember the most recent pulse
# initally set to 'low pulse' for each input
# When a pulse is received, the conjunction module first updates
# its memory for that input. Then, if it remembers high pulses for all inputs,
# it sends a low pulse; otherwise, it sends a high pulse.

# broadcast module (named broadcaster).
# When it receives a pulse, it sends the same pulse to all of its destination modules.

# button module.
# When you push the button, a single low pulse is sent directly to the broadcaster
# DO NOT push again until all pulses have been distributed / processed

# Pulses should be processed in the order they are sent

# Goal:
# For 1,000 button pushes
# What do you get if you multiply
# the total number of low pulses sent by the total number of high pulses sent?


def press_button(modules, signal_queue, high_pulses_sent, low_pulses_sent):
    # Capture button to broadcaster pulse
    low_pulses_sent += 1
    targets = modules['broadcaster']
    for t in targets:
        signal_queue.put((t, 'low', 'broadcaster'))
        low_pulses_sent += 1

    return high_pulses_sent, low_pulses_sent


def flip_flop(modules, module, flip_flop_dict, pulse, signal_queue, high_pulses_sent, low_pulses_sent):
    # If you get a high pulse then ignore it
    if pulse[1] == 'high':
        return high_pulses_sent, low_pulses_sent
    else:
        # flip status
        if flip_flop_dict[module] == False:
            flip_flop_dict[module] = True
            for t in modules[module]:
                signal_queue.put((t, 'high', module))
                high_pulses_sent += 1
        else:
            flip_flop_dict[module] = False
            for t in modules[module]:
                signal_queue.put((t, 'low', module))
                low_pulses_sent += 1

    return high_pulses_sent, low_pulses_sent


def conj(modules, module, conj_dict, pulse, signal_queue, high_pulses_sent, low_pulses_sent):
    # idx = modules[module].index(pulse[2])
    if conj_dict[module][pulse[2]] == 'low':
        conj_dict[module][pulse[2]] = 'high'
    else:
        conj_dict[module][pulse[2]] = 'low'

    # if all(x == 'high' for x in conj_dict[module]):
    if all(value == 'high' for value in conj_dict[module].values()):
        for t in modules[module]:
            signal_queue.put((t, 'low', module))
            low_pulses_sent += 1
    else:
        for t in modules[module]:
            signal_queue.put((t, 'high', module))
            high_pulses_sent += 1

    return high_pulses_sent, low_pulses_sent


def day_20(path):
    modules = {}
    conj_dict = {}
    flip_flop_dict = {}
    signal_queue = Queue()
    high_pulses_sent = 0
    low_pulses_sent = 0

    # Creating our data structures
    with open(path, "r") as f:
        for line in f.readlines():
            a, b = line.split('->')
            a = a.strip()
            b = list(map(str.strip, b.strip().split(',')))
            if "%" in a:
                modules[a[1:]] = b
                # Initailly set to off / False
                flip_flop_dict[a[1:]] = False
            elif "&" in a:
                modules[a[1:]] = b
                # Need to store the most recent pulse here..
                conj_dict[a[1:]] = {}
            else:
                modules[a] = b

    # Build the dictionary for the conj modules
    for t_key in modules.keys():
        for t in modules[t_key]:
            if t in conj_dict.keys():
                conj_dict[t][t_key] = 'low'

    for x in range(0, 1000):
        high_pulses_sent, low_pulses_sent = press_button(
            modules, signal_queue, high_pulses_sent, low_pulses_sent)

        while not signal_queue.empty():
            cur_signal = signal_queue.get()

            if cur_signal[0] in flip_flop_dict.keys():
                high_pulses_sent, low_pulses_sent = flip_flop(modules, cur_signal[0],
                                                              flip_flop_dict, cur_signal, signal_queue, high_pulses_sent, low_pulses_sent)
                # flip_flop(modules, module, flip_flop_dict, pulse, signal_queue):
            elif cur_signal[0] in conj_dict.keys():
                high_pulses_sent, low_pulses_sent = conj(modules, cur_signal[0],
                                                         conj_dict, cur_signal, signal_queue, high_pulses_sent, low_pulses_sent)

    print(
        f'Part 1 answer: {low_pulses_sent*high_pulses_sent}. Low: {low_pulses_sent} high: {high_pulses_sent}')


start_time = time.time()

day_20("./inputs/day_20_sample.txt")
# day_20("./inputs/day_20_input.txt")
print("--- %s seconds ---" % (time.time() - start_time))

# t = ['low' for x in range(0, len('add'))]
# print(t)
