# 과제3: 위상 정렬(이코테)
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024-11-01

from collections import deque
v, e = map(int, input().split())

indegree = [0] * (v+1)

graph = [[]for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    
    for i in result:
        print(i, end=' ')

topology_sort()