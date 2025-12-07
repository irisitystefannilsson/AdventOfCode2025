import time

def advent6_1():
    file = open('input06.txt')
    numbers = list()
    operators = list()
    for line in file:
        line = line.lstrip(' ').strip('\n').strip(' ').split()
        if line[0].isnumeric():
            numbers.append(line)
        else:
            operators.append(line)

    grand = 0
    for i in range(len(operators[0])):
        if operators[0][i] == '+':
            sum = 0
            for num in numbers:
                sum += int(num[i])
            grand += sum
        elif operators[0][i] == '*':
            prod = 1
            for num in numbers:
                prod *= int(num[i])
            grand += prod

    print('Grand total(1): ', grand)


def find_digit_idxs(line : str, start : int):
    index = start
    while line[index] == ' ':
        index += 1
    first = index
    while line[index].isnumeric():
        index += 1
        if (index == len(line)):
            return first, index - 1
    return first, index - 1


def advent6_2():
    file = open('input06.txt')
    numbers = list()
    operators = list()
    for line in file:
        line = line.strip('\n')
        if line.lstrip(' ')[0].isnumeric():
            numbers.append(line)
        else:
            operators.append(line.lstrip(' ').strip(' ').split())

    operands = list()
    for i in range(len(operators[0])):
        operands.append([])
    for r in numbers:
        end = -1
        for i in range(len(operators[0])):
            start, end = find_digit_idxs(r, end + 1)
            operands[i].append([start, end])
            
    grand = 0
    for i in range(len(operators[0])):
        max_end = 0
        min_start = 10000000000
        for op in operands[i]:
            max_end = max(max_end, op[1])
            min_start = min(min_start, op[0])
        if operators[0][i] == '+':
            sum = 0
            for j in range(min_start, max_end + 1):
                term = ''
                for num in numbers:
                    if num[j].isnumeric():
                        term += num[j]
                sum += int(term)
            grand += sum
        elif operators[0][i] == '*':
            prod = 1
            for j in range(min_start, max_end + 1):
                fakt = ''
                for num in numbers:
                    if num[j].isnumeric():
                        fakt += num[j]
                prod *= int(fakt)
            grand += prod

    print('Grand total(2): ', grand)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 6')
    advent6_1()
    advent6_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
