import time

def advent3_1():
    file = open('input03.txt')
    bank_sum = 0
    for line in file:
        bank = line.strip('\n')
        max_digit = 0
        it = 0
        for it in range(len(bank) - 1):
            max_digit = max(max_digit, int(bank[it]))
        for it in range(len(bank) - 1):
            if int(bank[it]) == max_digit:
                break
        next_digit = 0
        for it in range(it + 1, len(bank)):
            next_digit = max(next_digit, int(bank[it]))
        bank_sum += int(str(max_digit) + str(next_digit))
    print('Joltage(1): ', bank_sum)
    

def find_max_digit(bank : str, start_dist : int, end_dist : int):
    max_digit = 0
    it = 0
    for it in range(start_dist, len(bank) - end_dist):
        max_digit = max(max_digit, int(bank[it]))
    for it in range(start_dist, len(bank) - end_dist):
        if int(bank[it]) == max_digit:
            break
    return max_digit, it


def advent3_2():
    file = open('input03.txt')
    bank_sum = 0
    for line in file:
        bank = line.strip('\n')
        pos = -1
        digits = ''
        for num in range(12):
            dig, pos = find_max_digit(bank, pos + 1, 11 - num)
            digits += str(dig)
        bank_sum += int(digits)
    print('Joltage(2): ', bank_sum)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 3')
    advent3_1()
    advent3_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
