import sys

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2, wt):

        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt

    def getMinVertex(self, visited, weight):

        min_vertex = -1

        for i in range(self.nVertices):

            if visited[i] == False and (min_vertex == -1 or weight[min_vertex] > weight[i]):
                min_vertex = i

        return min_vertex

    def prims(self):

        visited = [False for i in range(self.nVertices)]
        weight = [sys.maxsize for i in range(self.nVertices)]
        parent = [-1 for i in range(self.nVertices)]

        weight[0] = 0

        for i in range(self.nVertices - 1):

            min_vertex = self.getMinVertex(visited, weight)
            visited[min_vertex] = True

            # exploring neighbors and updating the value

            for j in range(self.nVertices):

                if self.adjMatrix[min_vertex][j] > 0 and visited[j] == False:

                    if weight[j] > self.adjMatrix[min_vertex][j]:
                        weight[j] = self.adjMatrix[min_vertex][j]

                        parent[j] = min_vertex

            # print
        for i in range(1, self.nVertices):

            if i < parent[i]:
                print(str(i) + " " + str(parent[i]) + " " + str(weight[i]))

            else:
                print(str(parent[i]) + " " + str(i) + " " + str(weight[i]))


li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]
g = Graph(n)

for i in range(n):
    curr = [int(ele) for ele in input().split()]
    g.addEdge(curr[0], curr[1], curr[2])

g.prims()
'''
I/P:
3 3
1 2 6
2 0 2
1 0 2
'''
'''
O/P:

0 1 2
0 1 2

'''