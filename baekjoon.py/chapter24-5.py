import sys
input = sys.stdin.readline

# 입력: n x n 크기의 2차원 배열과 쿼리의 개수 m
n, m = map(int, input().split())

# 2차원 배열 arr을 입력받음
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

# dp 배열을 초기화 (n+1 x n+1 크기)
# dp[i][j]는 (1,1)부터 (i,j)까지의 부분합을 저장
dp = [[0]*(n+1) for i in range(n+1)]

# dp 배열을 채움
for i in range(1, n+1):
    for j in range(1, n+1):
        # (i,j)까지의 부분합을 계산
        # dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]은 중복 덧셈을 제거하기 위한 것
        # arr[i-1][j-1]은 현재 위치의 값을 더함
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

# 쿼리를 처리
for k in range(m):
    # 쿼리 입력: (x1, y1)부터 (x2, y2)까지의 부분합을 구함
    x1, y1, x2, y2 = map(int, input().split())
    
    # (x1, y1)부터 (x2, y2)까지의 부분합을 계산
    # dp[x2][y2]는 (1,1)부터 (x2, y2)까지의 부분합
    # dp[x2][y1-1]와 dp[x1-1][y2]는 중복 덧셈을 제거하기 위한 것
    # dp[x1-1][y1-1]는 중복 제거된 부분을 다시 더함
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    
    # 결과 출력
    print(result)
