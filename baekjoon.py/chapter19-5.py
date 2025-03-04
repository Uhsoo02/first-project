import sys
input = sys.stdin.readline

def bridge(n, m):
    # dp 테이블 초기화: dp[i][j]는 i개의 다리를 j개의 지점에 놓을 수 있는 경우의 수
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)] 
    
    # N = 1일 때, 다리를 놓을 수 있는 경우의 수는 M개
    for i in range(1, m+1): 
        dp[1][i] = i

    # N이 2 이상일 때, 다리를 놓을 수 있는 경우의 수 계산
    for i in range(2, n+1): 
        for j in range(i, m+1):
            # k는 j부터 i-1까지 역순으로 반복
            for k in range(j, i-1, -1):
                # dp[i][j]에 dp[i-1][k-1]을 더함
                dp[i][j] += dp[i-1][k-1]

    # 최종 결과 반환
    return dp[n][m]

# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스에 대해 반복
for _ in range(T):
    # N과 M 값을 입력받음
    N, M = map(int, input().split())
    # bridge 함수를 호출하여 결과 출력
    print(bridge(N, M))
