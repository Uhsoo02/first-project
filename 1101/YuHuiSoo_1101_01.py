# 과제1: 팩토리얼 하향식 상향식 축소 정복기법
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024-11-01

def factorial_recur (n):
    if n == 1:
        return 1
    else :
        return n * factorial_recur(n-1)
    
def factorial_iter(n):
    result = 1
    for k in range(n, 0, -1):
        result = result * k
    return result

n = int(input("정수 n을 입력하세요.: "))

print(f"하향식(순환) Factorial({n}) = {factorial_recur(n)}")
print(f"상향식(반복) Factorial({n}) = {factorial_iter(n)}")