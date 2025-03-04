n = int(input())
arr = list(map(int, input().split()))

dp1 = [1] * n
dp2 = [1] * n

# dp1: 왼쪽에서 오른쪽으로 가는 최장 증가 부분 수열
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

# dp2: 오른쪽에서 왼쪽으로 가는 최장 감소 부분 수열
for i in range(n-2, -1, -1):
    for j in range(i+1, n):
        if arr[j] < arr[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

# dp3: 바이토닉 수열의 길이 계산
dp3 = [dp1[i] + dp2[i] - 1 for i in range(n)]

print(max(dp3))
