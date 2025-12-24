import time

def area(corner1, corner2):
    return (abs(corner1[0] - corner2[0]) + 1)*(abs(corner1[1] - corner2[1]) + 1)


def advent9_1():
    file = open('input09.txt')
    corners = list()
    for line in file:
        line = line.strip('\n').split(',')
        corners.append((int(line[0]), int(line[1])))

    areas = list()
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            areas.append(area(corners[i], corners[j]))

    areas = sorted(areas)
    print('Max area(1):', areas[-1])
        

class Edge:
    def __init__(self, start : tuple, end : tuple):
        if start[0] != end[0]:
            self.start = (min(start[0], end[0]), start[1])
            self.end = (max(start[0], end[0]), start[1])
        else:
            self.start = (start[0], min(start[1], end[1]))
            self.end = (start[0], max(start[1], end[1]))      

    def intersects(self, other : 'Edge'):
        if other.start[0] == other.end[0]:
            if self.start[0] != self.end[0]:
                if self.start[0] < other.end[0] < self.end[0]:
                    if other.start[1] < self.end[1] < other.end[1]:
                        return True, (0, 0)
                if self.start[1] == other.start[1]:
                    if self.start[0] < other.end[0] < self.end[0]:
                        return True, (other.start[0], other.start[1] + 1)
                if self.start[1] == other.end[1]:
                    if self.start[0] < other.end[0] < self.end[0]:
                        return True, (other.end[0], other.end[1] - 1)                    
        else:
            if self.start[1] != self.end[1]:
                if self.start[1] < other.end[1] < self.end[1]:
                    if other.start[0] < self.end[0] < other.end[0]:
                        return True, (0, 0)
                if self.start[0] == other.start[0]:
                    if self.start[1] < other.end[1] < self.end[1]:
                        return True, (other.start[0] + 1, other.start[1])
                if self.start[0] == other.end[0]:
                    if self.start[1] < other.end[1] < self.end[1]:
                        return True, (other.end[0] - 1, other.end[1])                    
        return False, (0, 0)


def inside(corner1 : tuple, corner2 : tuple, pos : tuple):
    if (min(corner1[0], corner2[0]) < pos[0] < max(corner1[0], corner2[0])) and (min(corner1[1], corner2[1]) < pos[1] < max(corner1[1], corner2[1])):
        return True
    return False


def intersection(corner1 : tuple, corner2 : tuple, edges : list):
    edge1 = Edge(corner1, (corner1[0], corner2[1]))
    edge2 = Edge(corner1, (corner2[0], corner1[1]))
    edge3 = Edge(corner2, (corner2[0], corner1[1]))
    edge4 = Edge(corner2, (corner1[0], corner2[1]))
    for edge in [edge1, edge2, edge3, edge4]:
        for other_edges in edges:
            inter, pos = edge.intersects(other_edges)
            if inter and pos == (0, 0):
                return True
            elif inter:
                if inside(corner1, corner2, pos):
                    return True
    return False

        
def advent9_2():
    file = open('input09.txt')
    corners = list()
    for line in file:
        line = line.strip('\n').split(',')
        corners.append((int(line[0]), int(line[1])))

    edges = list()
    for i in range(len(corners) - 1):
        edges.append(Edge(corners[i], corners[i + 1]))
    edges.append(Edge(corners[-1], corners[0]))

    areas = list()
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            if not intersection(corners[i], corners[j], edges):
                areas.append(area(corners[i], corners[j]))

    areas = sorted(areas)
    print('Max read-green area(2):', areas[-1])

if __name__ == '__main__':

    start_time = time.time()
    print('Advent 9')
    advent9_1()
    advent9_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
