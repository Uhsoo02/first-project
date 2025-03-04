# 과제1: Floyd 최단 경로 탐색 알고리즘-가로세로노드 표시
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024-11-22

# Modified Floyd-Warshall Algorithm Code with Row and Column Labels

import copy

# Floyd-Warshall Algorithm with readable matrix display
def shortest_path_floyd(vertex, weight):
    vsize = len(vertex)
    D = copy.deepcopy(weight)

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
        print_with_labels(vertex, D) # Print the matrix with la

def print_with_labels(vertex, D):
    vsize = len(D)
    print("\n=========================================")
    print("     ", end = "")
    for v in vertex:
        print(f"{v:>5}", end="")
    print("\n-----------------------------------------")
    for i in range(vsize):
        print(f"{vertex[i]:<5}", end="")
        for j in range(vsize):
            if D[i][j] == float('inf'):
                print(f"{'INF':>5}", end="")
            else:
                print(f"{D[i][j]:>5}", end="")
        print()
    print("=========================================")

# Example graph
INF = float('inf')
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [
    [0, 7, INF, INF, 3, INF, INF],
    [7, 0, 4, 6, INF, INF, INF],
    [INF, 4, 0, 2, INF, INF, INF],
    [INF, 6, 2, 0, INF, 9, INF],
    [3, INF, INF, INF, 0, 10, 4],
    [INF, INF, INF, 9, 10, 0, 5],
    [INF, INF, INF, INF, 4, 5, 0]
]

# Run the algorithm
print("Shortest Path By Floyd's Algorithm")
shortest_path_floyd(vertex, weight)