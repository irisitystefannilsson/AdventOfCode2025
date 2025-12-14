import time


def distance(c1, c2):
    dist = abs(c1[0] - c2[0])**2 + abs(c1[1] - c2[1])**2 + abs(c1[2] - c2[2])**2
    return dist

def advent8_1():
    file = open('input08.txt')
    junctions = list()
    for line in file:
        line = line.strip('\n').split(',')
        junctions.append((int(line[0]), int(line[1]), int(line[2])))

    distances = list()
    for i in range(len(junctions)):
        for j in range(i + 1, len(junctions)):
            distances.append([distance(junctions[i], junctions[j]), [i, j]])
    distances = sorted(distances, key=lambda e: e[0])
    circuits = list()
    for i in range(1000):
        add_new = True
        found = list()
        for c in range(len(circuits)):
            if distances[i][1][0] in circuits[c]:
                add_new = False
                found.append((c, distances[i][1][1], circuits[c]))
            if distances[i][1][1] in circuits[c]:
                add_new = False
                found.append((c, distances[i][1][0], circuits[c]))
        if add_new:
            connected = set()
            connected.add(distances[i][1][0])
            connected.add(distances[i][1][1])
            circuits.append(connected)
        elif len(found) == 1:
            circuits[found[0][0]].add(found[0][1])
        elif len(found) == 2 and found[0][0] != found[1][0]:
            circuits.append(circuits[found[0][0]].union(circuits[found[1][0]]))
            circuits.remove(found[0][2])
            circuits.remove(found[1][2])
    circuits = sorted(circuits, key=lambda e: len(e))
    cprod = len(circuits[-1]) * len(circuits[-2]) * len(circuits[-3])
    print('Circuit product(1): ', cprod)


def advent8_2():
    file = open('input08.txt')
    junctions = list()
    for line in file:
        line = line.strip('\n').split(',')
        junctions.append((int(line[0]), int(line[1]), int(line[2])))

    distances = list()
    for i in range(len(junctions)):
        for j in range(i + 1, len(junctions)):
            distances.append([distance(junctions[i], junctions[j]), [i, j]])
    distances = sorted(distances, key=lambda e: e[0])
    circuits = list()
    for i in range(1000000):
        add_new = True
        found = list()
        for c in range(len(circuits)):
            if distances[i][1][0] in circuits[c]:
                add_new = False
                found.append((c, distances[i][1][1], circuits[c]))
            if distances[i][1][1] in circuits[c]:
                add_new = False
                found.append((c, distances[i][1][0], circuits[c]))
        if add_new:
            connected = set()
            connected.add(distances[i][1][0])
            connected.add(distances[i][1][1])
            circuits.append(connected)
        elif len(found) == 1:
            circuits[found[0][0]].add(found[0][1])
        elif len(found) == 2 and found[0][0] != found[1][0]:
            circuits.append(circuits[found[0][0]].union(circuits[found[1][0]]))
            circuits.remove(found[0][2])
            circuits.remove(found[1][2])
        if len(circuits) == 1 and len(circuits[0]) == len(junctions):
            print('Circuit product(2): ', junctions[distances[i][1][0]][0]*junctions[distances[i][1][1]][0])
            break


if __name__ == '__main__':

    start_time = time.time()
    print('Advent 8')
    advent8_1()
    advent8_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
