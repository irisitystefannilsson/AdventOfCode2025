import time

def advent5_1():
    file = open('input05.txt')
    rngs = list()
    line = file.readline().strip('\n')
    while line != '':
        rngs.append(line.split('-'))
        line = file.readline().strip('\n')
    ingredients = list()
    line = file.readline().strip('\n')
    while line != '':
        ingredients.append(line)
        line = file.readline().strip('\n')

    nof_fresh = 0
    for ingredient in ingredients:
        for rng in rngs:
            if int(rng[0]) <= int(ingredient) <= int(rng[1]):
                nof_fresh += 1
                break
    print('Fresh ingredients(1): ', nof_fresh)


def overlap(first :list, second : list):
    if (second[0] <= first[0] <= second[1]) or (second[0] <= first[1] <= second[1]):
        return True, [min(first[0], second[0]), max(first[1], second[1])]
    return False, first


def contained(first :list, second : list):
    if (second[0] <= first[0]) and (first[1] <= second[1]):
        return True
    return False


def merge_range(rng : list, rngs : list):
    for other in rngs:
        is_overlap, new_rng = overlap(rng, other)
        if is_overlap:
            rng = new_rng
    return rng


def advent5_2():
    file = open('input05.txt')
    rngs = list()
    line = file.readline().strip('\n')
    while line != '':
        rng = line.split('-')
        rngs.append([int(rng[0]), int(rng[1])])
        line = file.readline().strip('\n')
        
    merged_rngs0 = list()
    for rng in rngs:
        merged = merge_range(rng, rngs)
        if merged not in merged_rngs0:
            merged_rngs0.append(merged)
        
    merged_rngs = list()
    for rng in merged_rngs0:
        merged = merge_range(rng, merged_rngs0)
        if merged not in merged_rngs:
            merged_rngs.append(merged)

    exclusive_rngs = list()
    for index1 in range(len(merged_rngs)):
        exclusive = True
        for index2 in range(len(merged_rngs)):
            if index1 != index2:
                if contained(merged_rngs[index1], merged_rngs[index2]):
                    exclusive = False
        if exclusive:
            if merged_rngs[index1] not in exclusive_rngs:
                exclusive_rngs.append(merged_rngs[index1])

    nof_fresh = 0
    for r in exclusive_rngs:
        nof_fresh += r[1] - r[0] + 1
    print('Nof fresh(2): ', nof_fresh)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 5')
    advent5_1()
    advent5_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
