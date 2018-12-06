from elice_utils import EliceUtils

elice_utils = EliceUtils()


def main():
    exampleGraph = [[0.0, 7.0, 0.0, 0.0, 1.0],
                    [7.0, 0.0, 6.0, 0.0, 5.0],
                    [0.0, 6.0, 0.0, 2.0, 3.0],
                    [0.0, 0.0, 2.0, 0.0, 4.0],
                    [1.0, 5.0, 3.0, 4.0, 0.0]]
    exampleGraph2 = [[0.0, 2.0, 3.0, 3.0, 0.0, 0.0, 0.0],
                     [2.0, 0.0, 4.0, 0.0, 3.0, 0.0, 0.0],
                     [3.0, 4.0, 0.0, 5.0, 1.0, 6.0, 0.0],
                     [3.0, 0.0, 5.0, 0.0, 0.0, 7.0, 0.0],
                     [0.0, 3.0, 1.0, 0.0, 0.0, 8.0, 0.0],
                     [0.0, 0.0, 6.0, 7.0, 8.0, 0.0, 9.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 9.0, 0.0]]

    MST = primAlgorithm(5, exampleGraph)

    for i in range(5):
        s = ""
        for j in range(5):
            s += (str(MST[i][j]) + " ")
        print(s)


# The assignment has 10 testcases.
# store indices of the testcases you want to skip
# for example: [9,10] => skip 9th and the last (10th) test cases
# store any number not within [1, ..., 10] if you don't want to skip any testcases
skipGrading = [0]


# PRIM'S ALGORITHM: Given a weighted connected undirected graph, compute a MST.
#      INPUT:   n: number of vertices
#               adj: adjacency matrix (2-dimensional array) with weights
#                   adj[0][3] (= adj[3][0]) is the weight of the edge between vertex 0 and vertex 3
#                   weight of an edge is a floating point number between [0.5, 1000]
#                   if there is no edge between i and j, adj[i][j] = 0
#      OUTPUT:  minTree: adjacency matrix (2-dimensional array) with boolean entries of the MST
#                   minTree[i][j] = True if the MST has an edge between the vertex i and j
#                   minTree[i][j] = False if the MST has no edge between the vertex i and j
def primAlgorithm(n, adj):
    minTree = [x[:] for x in [[False] * n] * n]

    # implement here
    INF = 1001  # constant to represent infinite value

    # initialize unvisited vertices
    unvisited = list(range(n))

    # pick starting vertex, and update node values
    start = unvisited.pop()
    e_v = [start] * n
    d_v = [weight if weight > 0 else INF for weight in adj[start]]

    # traverse unvisited vertices
    while unvisited:
        # extract an unvisited vertex with minimum d_u
        u = 0
        min_du = INF
        for vertex in unvisited:
            if d_v[vertex] < min_du:
                min_du = d_v[vertex]
                u = vertex
        unvisited.remove(u)

        # add edge(u, e_u) to MST
        minTree[u][e_v[u]] = minTree[e_v[u]][u] = True

        # mark as visited
        d_v[u] = 0.0

        # update neighbors of extracted vertex
        for neighbor in unvisited:
            if 0 < adj[u][neighbor] < d_v[neighbor]:
                d_v[neighbor] = adj[u][neighbor]
                e_v[neighbor] = u

    return minTree


if __name__ == "__main__":
    main()
