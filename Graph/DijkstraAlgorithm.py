import sys


class Node:
    visited: bool
    previous: int
    distance: int

    def __init__(self):
        self.visited = False
        self.previous = -1
        self.distance = sys.maxsize

    def __str__(self):
        return f'{self.distance}'

    def __repr__(self):
        return f'{self.distance}'


def Dijkstra(graph, first):
    tab = []
    for i in range(len(graph)):
        tab.append(Node())
    tab[first].distance = 0
    a = first
    while a != -1:
        tab[a].visited = True
        for i in range(len(graph)):
            if graph[a][i] > 0 and tab[a].distance + graph[a][i] < tab[i].distance:
                tab[i].distance = tab[a].distance + graph[a][i]
                tab[i].previous = a
        a = -1
        dist = sys.maxsize
        for i in range(len(graph)):
            if not tab[i].visited and tab[i].distance < dist:
                a = i
                dist = tab[i].distance
    return tab


def sum(tab):
    result = 0
    for i in tab:
        result += i.distance
    return result


graph = [[0, 5, 3, 6, 7],
           [5, 0, 3, 8, 5],
           [3, 3, 0, 4, 7],
           [6, 8, 4, 0, 9],
           [7, 5, 7, 9, 0]]
for i in range(len(graph)):
    result = Dijkstra(graph, i)
    print(result)
    print(sum(result))

