# 물건의 개수 N과 배낭의 최대 무게 K를 입력받음
N, K = map(int, input().split())

# 각 물건의 무게 W와 가치 V를 저장할 리스트
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))  # (무게, 가치) 형태로 저장

# DP 배열을 초기화 (0 ~ K까지의 무게에 대해 가능한 최대 가치를 저장)
dp = [0] * (K + 1)

# 각 물건을 하나씩 확인
for W, V in items:
    # 무게 제한에서 역순으로 물건을 넣을 수 있는지 확인
    for current_weight in range(K, W - 1, -1):
        # 현재 물건을 넣었을 때 가치가 더 높다면 갱신
        dp[current_weight] = max(dp[current_weight], dp[current_weight - W] + V)

# 최대 가치 출력
print(dp[K])
