import time

def check_for_invalid_id(id : str):
    if len(id) % 2 == 1:
        return 0
    hlen = len(id) // 2
    if id[0:hlen] == id[hlen:]:
        return int(id)
    return 0


def advent2_1():
    file = open('input02.txt')
    sum_invalid_ids = 0 
    for line in file:
        ids = line.strip('\n').split(',')
        for id_range in ids:
            start_id, end_id = id_range.split('-')
            for id in range(int(start_id), int(end_id) + 1):
                sum_invalid_ids += check_for_invalid_id(str(id))
    print('Sum of invalid ids(1): ', sum_invalid_ids)
    

def check_for_silly_id(id : str):
    id_len = len(id)
    retval = 0
    for l in range(1, (id_len // 2) + 1):
        if id_len % l == 0:
            base = id[0:l]
            silly = True
            for r in range(1, (id_len // l)):
                if base != id[r*l:(r+1)*l]:
                    silly = False
                    break
            if silly:
                retval = int(id)
    return retval


def advent2_2():
    file = open('input02.txt')
    sum_invalid_ids = 0 
    for line in file:
        ids = line.strip('\n').split(',')
        for id_range in ids:
            start_id, end_id = id_range.split('-')
            for id in range(int(start_id), int(end_id) + 1):
                sum_invalid_ids += check_for_silly_id(str(id))
    print('Sum of invalid ids(1): ', sum_invalid_ids)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 2')
    advent2_1()
    advent2_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
