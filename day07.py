import time
import numpy as np

MAP_SIZE = (142, 141)

def beam_drop_step(coords : set, map):
    new_coords = set()
    nof_splits = 0
    for c in coords:
        if map[c[0] + 1, c[1]] == '^':
            nof_splits += 1
            new_coords.add((c[0] + 1, c[1] - 1))
            new_coords.add((c[0] + 1, c[1] + 1))
        else:
            new_coords.add((c[0] + 1, c[1]))
    return nof_splits, new_coords


def advent7_1():
    file = open('input07.txt');
    map = np.full(MAP_SIZE, '.', dtype=str)
    line_num = 0
    start = [0, 0]
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            map[line_num, ch] = row[ch]
            if row[ch] == 'S':
                start = [line_num, ch]
        line_num += 1
        
    coords = set()
    coords.add((start[0], start[1]))
    nof_splits = 0
    for s in range(MAP_SIZE[0] - 1):
        splits, coords = beam_drop_step(coords, map)
        nof_splits += splits
    print('''Nof splits(1):''', nof_splits)


def quantum_beam_drop_step(coords, map, row):
    new_coords = np.full(MAP_SIZE[1], 0, dtype=int)
    for c in range(MAP_SIZE[1]):
        if map[row][c] == '^':
            new_coords[c - 1] += coords[c] 
            new_coords[c + 1] += coords[c] 
        else:
            new_coords[c] += coords[c]
    return new_coords


def advent7_2():
    file = open('input07.txt');
    map = np.full(MAP_SIZE, '.', dtype=str)
    line_num = 0
    start = [0, 0]
    for line in file:
        row = line.strip('\n')
        for ch in range(len(row)):
            map[line_num, ch] = row[ch]
            if row[ch] == 'S':
                start = [line_num, ch]
        line_num += 1
        
    coords = np.full(MAP_SIZE[1], 0, dtype=int)
    coords[start[1]] = 1
    for s in range(1, MAP_SIZE[0] - 1):
        coords = quantum_beam_drop_step(coords, map, s)
    print('''Nof quantum paths(2):''', sum(coords))


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 7')
    advent7_1()
    advent7_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
