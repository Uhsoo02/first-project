# 과제5: 최근접 쌍의 거리
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024-11-12

import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2)

def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(p[i], p[j])
            if dist < mindist:
                mindist = dist
    return mindist

def strip_closest(P, d):
    n = len(P)
    d_min = d
    P.sort(key = lambda point: point[1])

    for i in range(n):
        j = i + 1
        while j < n and (P[j][i] - P[i][1]) < d_min:
            dij = dist(P[i], p[j])
            if dij < d_min:
                d_min = dij
            j += 1
    return d_min

def closest_pait_dist(P, n):
    if n <= 3:
        return closest_pair(P)
    
    mid = n // 2
    mid_x = P[mid][0]

    dl = closest_pait_dist(P[:mid], mid)
    dr = closest_pait_dist(P[mid:], n-mid)
    d = min(dl, dr)

    Pm = []
    for i in range(n):
        if abs(P[i][0] - mid_x) < d:
            Pm.append(P[i])

    ds = strip_closest(Pm, d)
    return min(d, ds)

p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
p.sort(key = lambda point: point[0])
print("가장 가까운 두 점의 거리", closest_pait_dist(p, len(p)))