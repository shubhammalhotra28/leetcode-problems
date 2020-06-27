class Edge:

    def __init__(self, src, dest, wt):
        self.src = src
        self.wt = wt
        self.dest = dest


def getParent(v, parent):
    if v == parent[v]:
        return v

    return getParent(parent[v],parent)

def kruskal(edges, nVertices):
    parent = [i for i in range(nVertices)]
    edges = sorted(edges, key=lambda edge: edge.wt)

    count = 0
    output = []

    i = 0
    while count < (nVertices - 1):

        currentEdge = edges[i]
        srcParent = getParent(currentEdge.src, parent)
        destParent = getParent(currentEdge.dest, parent)

        if srcParent != destParent:
            output.append(currentEdge)
            count += 1
            parent[srcParent] = destParent
        i += 1

    return output


li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]
edges = []

for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    src = curr_input[0]
    dest = curr_input[1]
    wt = curr_input[2]
    edge = Edge(src, dest, wt)
    edges.append(edge)

output = kruskal(edges, n)


# edge will have source, destination and weights

for currEdge in output:
    if currEdge.src < currEdge.dest:
        print(str(currEdge.src)+" "+str(currEdge.dest)+" "+str(currEdge.wt))
    else:
        print(str(currEdge.dest) + " " + str(currEdge.src) + " " + str(currEdge.wt))
