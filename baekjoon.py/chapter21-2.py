def fibonachi(n):
    # 기저 조건: n이 1 이하일 때, n을 그대로 반환
    if n <= 1:
        return n
    # 재귀 호출: n번째 피보나치 수는 (n-1)번째와 (n-2)번째 피보나치 수의 합
    return fibonachi(n-1) + fibonachi(n-2)

# 사용자로부터 정수 n을 입력받음
n = int(input())
# n번째 피보나치 수를 계산하여 출력
print(fibonachi(n))
