## Read input as specified in the question.
## Print output as specified in the question.
import sys


class Graph:

    def __init__(self, nVertices):

        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(nVertices)] for i in range(nVertices)]

    def addEdge(self, v1, v2, dist):

        self.adjMatrix[v1][v2] = dist
        self.adjMatrix[v2][v1] = dist

    def getMin(self, visited, dist):

        min_vertex = -1

        for i in range(self.nVertices):

            if visited[i] == False and (min_vertex == -1 or dist[min_vertex] > dist[i]):
                min_vertex = i

        return min_vertex

    def dijkstra(self):

        visited = [False for i in range(self.nVertices)]

        dist = [sys.maxsize for i in range(self.nVertices)]
        dist[0] = 0

        for i in range(self.nVertices - 1):

            min_vertex = self.getMin(visited, dist)
            visited[min_vertex] = True

            for j in range(self.nVertices):

                if visited[j] == False and self.adjMatrix[min_vertex][j] > 0:

                    if dist[j] > dist[min_vertex] + self.adjMatrix[min_vertex][j]:
                        dist[j] = dist[min_vertex] + self.adjMatrix[min_vertex][j]

        for i in range(self.nVertices):
            print(str(i) + " " + str(dist[i]))


li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]
g = Graph(n)

for i in range(n):
    arr = [int(ele) for ele in input().split()]

    v1 = arr[0]
    v2 = arr[1]
    dist = arr[2]
    g.addEdge(v1, v2, dist)

g.dijkstra()


'''
I/P
3 3
1 2 6
2 0 2
1 0 2
'''
'''
O/p:
0 0
1 2
2 2 
'''





