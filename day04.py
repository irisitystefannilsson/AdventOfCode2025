import time
import numpy as np

MAP_SIZE = (137, 137)

def is_accessible(coords, map):
    nof_close_rolls = 0
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == 0 and c == 0:
                continue
            if (0 <= coords[0] + r < MAP_SIZE[0]) and (0 <= coords[1] + c < MAP_SIZE[1]):
                if map[coords[0] + r][coords[1] + c] == '@':
                    nof_close_rolls += 1
    return nof_close_rolls < 4

    
def advent4_1():
    file = open('input04.txt');
    map = np.full(MAP_SIZE, '.', dtype=str)
    line_num = 0
    rolls = list()
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            map[line_num, ch] = row[ch]
            if row[ch] == '@':
                rolls.append([line_num, ch])
        line_num += 1
    accessible = 0
    for roll in rolls:
        if is_accessible(roll, map):
            accessible += 1
    print('''Nof accessible rolls(1):''', accessible)
    

def advent4_2():
    file = open('input04.txt');
    map = np.full(MAP_SIZE, '.', dtype=str)
    line_num = 0
    rolls = list()
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            map[line_num, ch] = row[ch]
            if row[ch] == '@':
                rolls.append([line_num, ch])
        line_num += 1
    accessible = 0
    some_accessible = True
    while some_accessible:
        some_accessible = False
        to_remove = list()
        for roll in rolls:
            if is_accessible(roll, map):
                some_accessible = True
                accessible += 1
                to_remove.append(roll)
        for rroll in to_remove:
            map[rroll[0]][rroll[1]] = '.'
            rolls.remove(rroll)
    print('''Nof accessible rolls(2):''', accessible)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 4')
    advent4_1()
    advent4_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
