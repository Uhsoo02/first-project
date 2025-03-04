# 하노이 탑 문제를 해결하는 재귀 함수
def Hanoi_top(n, start, end):
    # 기저 조건: 원판이 1개일 때, 시작 기둥에서 목표 기둥으로 옮김
    if n == 1:
        print(start, end)
        return
    
    # 1단계: n-1개의 원판을 시작 기둥에서 중간 기둥으로 옮김
    Hanoi_top(n-1, start, 6-start-end)
    # 2단계: 가장 큰 원판을 시작 기둥에서 목표 기둥으로 옮김
    print(start, end)
    # 3단계: n-1개의 원판을 중간 기둥에서 목표 기둥으로 옮김
    Hanoi_top(n-1, 6-start-end, end)

# 사용자로부터 원판의 개수 n을 입력받음
n = int(input())
# 하노이 탑 문제의 최소 이동 횟수를 계산하여 출력
print(2**n - 1)
# 하노이 탑 문제를 해결하는 함수를 호출하여 이동 과정을 출력
Hanoi_top(n, 1, 3)
