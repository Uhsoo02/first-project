def topological_sort(graph):
    inDeg = {}
    for v in graph:
        inDeg[v] = 0
    for v in graph:
        for u in graph[v]:
            inDeg[u] += 1

    vlist = []
    for v in graph:
        if inDeg[v] == 0:
            vlist.append(v)

    while vlist:
        v = vlist.pop()
        print(v, end=' ')
        for u in graph[v]:
            inDeg[u] -= 1
            if inDeg[u] == 0:
                vlist.append(u)

mygraph = {
    "A": {"C", "D"},
    "B": {"C", "D", "E"},
    "C": {"E"},
    "D": {"F"},
    "E": {"F"},
    "F": set()
}

print('topological_sort:')
topological_sort(mygraph)
print()
