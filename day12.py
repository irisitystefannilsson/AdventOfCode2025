import time
import numpy as np

SHAPE_SIZE = (3, 3)

class Present:
    def __init__(self):
        self.shape = np.full(SHAPE_SIZE, '.', dtype=str)

    def min_cover(self):
        cover = 0
        for r in [0, 1, 2]:
            for c in [0, 1, 2]:
                if self.shape[r, c] == '#':
                    cover += 1
        return cover
    
def advent12():
    file = open('input12.txt');
    presents = list()
    domains = list()
    nof_presents_per_domain = list()
    line = file.readline().strip('\n')
    while True:
        if len(presents) < 6 and line[1] == ':':
            present = Present()
            for r in [0, 1, 2]:
                line = file.readline().strip('\n')
                for ch in [0, 1, 2]:
                    present.shape[r, ch] = line[ch]
            presents.append(present)
            file.readline()
            line = file.readline().strip('\n')
        else:
            if line == '':
                break
            size, nof_presents = line.split(':')
            domains.append(size.split('x'))
            nof_presents_per_domain.append(nof_presents.lstrip(' ').split(' '))
            line = file.readline().strip('\n')
            
    nof_fits = 0
    nof_non_fits = 0
    all_handled = True
    for p in range(len(domains)):
        area = int(domains[p][0])*int(domains[p][1])
        max_cover = 0
        min_cover = 0
        for t in range(len(nof_presents_per_domain[p])):
            max_cover += int(nof_presents_per_domain[p][t])*9
            min_cover += int(nof_presents_per_domain[p][t])*presents[t].min_cover()
        if area >= max_cover:
            nof_fits += 1
        elif area < min_cover:
            nof_non_fits += 1
        else:
            all_handled = False

    if all_handled:
        print('Nof fitting presents/regions:', nof_fits)
    else:
        print('...not all were handled directly!')

if __name__ == '__main__':

    start_time = time.time()
    print('Advent 12')
    advent12()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
