import time


def advent1_1():
    file = open('input01.txt')
    rots = list()
    for line in file:
        rots.append(line.strip('\n'))

    loc = 50
    zero_count = 0
    for rot in rots:
        if rot[0] == 'L':
            loc = (loc - int(rot[1:])) % 100
        elif rot[0] == 'R':
            loc = (loc + int(rot[1:])) % 100
        if loc == 0:
            zero_count += 1
    print('Passwd(1): ', zero_count)


def advent1_2():
    file = open('input01.txt')
    rots = list()
    for line in file:
        rots.append(line.strip('\n'))

    loc = 50
    zero_count = 0
    for rot in rots:
        if rot[0] == 'L':
            incr = int(rot[1:])
            if incr >= loc and loc != 0:
                zero_count += 1
            zero_count += abs(incr - loc) // 100
            loc = (loc - incr) % 100 
        elif rot[0] == 'R':
            incr = int(rot[1:])
            if (incr + loc) >= 100:
                zero_count += 1
            zero_count += abs(incr - (100 - loc)) // 100
            loc = (loc + incr) % 100
    print('Passwd(2): ', zero_count)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 1')
    advent1_1()
    advent1_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
