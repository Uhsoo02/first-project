# 과제2: 다익스트라
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024.12.13

def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)
    dist = list(adj[start])
    dist[start] = 0
    path = [start] * vsize
    found = [False] * vsize
    found[start] = True

    for i in range(vsize) :
        print("Step%2d: "%(i+1), dist)
        u = getMinVertex(dist, found)
        found[u] = True

        for w in range(vsize):
            if not found[w]:
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u

    return path

def getMinVertex(dist, selected) :
    minv = -1
    mindist = INF
    for v in range(len(dist)) :
        if not selected[v] and dist[v]<mindist:
            mindist = dist[v]
            minv = v
    return minv

INF = 9999
vertex = [  'A', 'B', 'C', 'D', 'E', 'F', 'G' ]
weight = [  [   0,  7, INF, INF,  3,  10, INF],
            [   7,  0,  4,  10,    2,  6, INF],
            [   INF,    4,  0,  2,  INF,    INF,    INF],
            [   INF,    10, 2,  0,  11, 9,  4],
            [   3,  2,  INF,    11, 0,  13, 5],
            [   10, 6,  INF,    9,  13, 0,  INF],
            [   INF,    INF,    INF,    4,  5,  INF,    0]]

print("Shortest Path By Dijkstra Algorithm")
start = 0
path = shortest_path_dijkstra(vertex, weight, start)

for end in range(len(vertex)) :
    if end != start:
        print("[최단경로: %s->%s] %s" %
                (vertex[start], vertex[end], vertex[end]), end = '')
        while (path[end] != start):
            print(" <- %s" % vertex[path[end]], end='')
            end = path[end]
        print(" <- %s" % vertex[path[end]])