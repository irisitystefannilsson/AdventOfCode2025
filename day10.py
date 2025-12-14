import time
import itertools
from mip import *

def test_solution(solution : list, coeffs : list, answer : list):
    for j in range(len(answer)):
        sum = 0
        for i in range(len(coeffs)):
            sum += solution[i]*coeffs[i][j]
        if sum % 2 != answer[j]:
            return False
    return True


def advent10_1():
    file = open('input10.txt')
    lights = list()
    buttons = list()
    for line in file:
        line = line.strip('\n').split(' ')
        light = line[0]
        lights.append(light)
        line.pop(0)
        line.pop(-1)
        buttons.append(line)

    fewest_presses = 0
    for l in range(len(lights)):
        coeffs = list()
        answer = list()
        light = lights[l].lstrip('[').strip(']')
        for i in range(len(light)):
            if light[i] == '.':
                answer.append(0)
            else:
                answer.append(1)
        for c in range(len(buttons[l])):
            coeffs.append([0]*len(light))
            lb = buttons[l][c].lstrip('(').strip(')').split(',')
            for coeff in lb:
                coeffs[-1][int(coeff)] = 1

        solutions = itertools.product([0, 1], repeat=len(buttons[l]))
        all_nof_press = list()
        for s in solutions:
            nof_press = 0
            if test_solution(s, coeffs, answer):
                for p in s:
                    if p == 1:
                        nof_press += 1
                all_nof_press.append(nof_press)
        fewest_presses += sorted(all_nof_press)[0]

    print('Fewest nof button presses(1):' , fewest_presses)


def advent10_2():
    file = open('input10.txt')
    jolts = list()
    buttons = list()
    for line in file:
        line = line.strip('\n').split(' ')
        jolt = line[-1]
        jolts.append(jolt)
        line.pop(0)
        line.pop(-1)
        buttons.append(line)

    fewest_presses = 0
    for l in range(len(jolts)):
        coeffs = list()
        answer = list()
        jolt = jolts[l].lstrip('{').strip('}').split(',')
        for i in range(len(jolt)):
            answer.append(int(jolt[i]))
        for c in range(len(buttons[l])):
            coeffs.append([0]*len(answer))
            lb = buttons[l][c].lstrip('(').strip(')').split(',')
            for coeff in lb:
                coeffs[-1][int(coeff)] = 1

        m = Model()
        y = [ m.add_var(var_type=INTEGER, lb=0) for i in range(len(buttons[l])) ]
        m.objective = xsum(y[i] for i in range(len(buttons[l])))
        for cons in range(len(answer)):
            m += xsum(coeffs[i][cons]*y[i] for i in range(len(buttons[l]))) == answer[cons] 
        m.optimize()
        for v in range(len(buttons[l])):
            fewest_presses += int(m.vars[v].x)

    print('Fewest button presses(2):', fewest_presses)


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 10')
    advent10_1()
    advent10_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
