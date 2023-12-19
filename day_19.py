import time
# Each part has a category
# x: Extremely cool looking
# m: Musical (it makes a noise when you hit it)
# a: Aerodynamic
# s: Shiny

# Each part goes through a workflow which may accept or reject the part

# the first rule that matches the part is applied imm.
# then the part moves to the destination described by the first rule

# All parts begin with the workflow "in"
# Add up all the parts that are accepted


# Part 2:  Each value x,m,a,s is between 0 and 4000
# How many distinct combinations would be accepted?

def calc_comp_val(val):
    values = ['x', 'm', 'a', 's']
    try:
        return values.index(val)
    except ValueError as e:
        return -1


def parse_rule(rule):
    # x, m, a, s

    if "<" not in rule and ">" not in rule:
        return rule, -1, False, False, 1
    elif "<" in rule:
        comparison_val = calc_comp_val(rule[0:1])
        return rule.split(":")[1], comparison_val, False, True, int(rule.split(":")[0].split("<")[1])
    elif ">" in rule:
        comparison_val = calc_comp_val(rule[0:1])
        return rule.split(":")[1], comparison_val, True, False, int(rule.split(":")[0].split(">")[1])


def day_19(path):
    accepted_parts = []
    workflows = {}
    # Creating our grid
    with open(path, "r") as f:
        data, parts = [x.splitlines() for x in f.read().split("\n\n")]
        parts = set(tuple(map(int, part.replace("{", "").replace("}", "").replace(
            ",", "=").split("=")[1: 8: 2])) for part in parts)

    for x in data:
        workflows[x.split("{")[0]] = list(
            x.split("{")[1].replace("}", "").split(","))
        # print(x.split("{")[1])

    for part in parts:
        state = 'in'
        instr_idx = 0

        while state not in ['A', 'R']:
            # if state in ['A', 'R']:
            #     final_state = state
            #     break
            # else:
            # current_workflow = workflows[state]
            # for rule in workflows[state]:
            rule = workflows[state][instr_idx]
            if rule == 'rfg':
                pass
            new_state, comparison_val, greater, lesser, threshold = parse_rule(
                rule)
            if greater:
                if part[comparison_val] > threshold:
                    # Go to the next workflow
                    state = new_state
                    instr_idx = 0
                else:
                    # go to the next rule
                    instr_idx += 1
            elif lesser:
                if part[comparison_val] < threshold:
                    # Go to the next workflow
                    state = new_state
                    instr_idx = 0
                else:
                    # go to the next rule
                    instr_idx += 1
            else:
                state = new_state
                instr_idx = 0

        if state == "A":
            accepted_parts.append(sum(part))
        # cannot go back to previous states
        # do we need to implement this or is this covered via the input?

    print(f'part 1 answer: {sum(accepted_parts)}')


start_time = time.time()

# day_19("./inputs/day_19_sample.txt")
day_19("./inputs/day_19_input.txt")
print("--- %s seconds ---" % (time.time() - start_time))

# print(calc_comp_val("t"))

# rule = 's<1351:px'
# print(rule.split(":")[0])
# print(rule.split(":")[0].split("<")[1])

# t = (2, 3)
# print(sum(t))
