class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, pred):
        sum = 0
        print("Krawędzie \tWaga")
        for i in range(0, self.V):
            print(pred[i], "-", i, "\t", self.graph[i][pred[i]])
            sum += self.graph[i][pred[i]]
        print(f'Suma: {sum}')

    def minKey(self, key, mstSet):
        min = float('inf')
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                minIndex = v
        return minIndex

    def primMST(self):
        key = [float('inf')] * self.V
        pred = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        pred[0] = -1
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if 0 < self.graph[u][v] < key[v] and mstSet[v] == False:
                    key[v] = self.graph[u][v]
                    pred[v] = u

        self.printMST(pred)


g = Graph(5)
g.graph = [[0, 5, 3, 6, 7],
           [5, 0, 3, 8, 5],
           [3, 3, 0, 4, 7],
           [6, 8, 4, 0, 9],
           [7, 5, 7, 9, 0]]
g.primMST()

