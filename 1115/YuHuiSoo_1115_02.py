# 과제2: 피보나치 수열(DP-수행시간) // 실습[2] = DP
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024-11-15

## DP로 구현한 피보나치 수열의 성능측정
import time

n = int(input("n을 입력하세요.:"))
dictionary = { 1: 1, 2: 1}
counter = 0

def fibo(n):
    global counter
    counter += 1
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibo(n-1) + fibo(n-2)
        dictionary[n] = output
        return output
    
start = time.time()
fibo(n)
end = time.time()

print("----------------------------------------------------")
print(f"fibo({n}) 계산에 활용될 덧셈 횟수는 {counter}번입니다.")
print("실행시간 =", end - start)
#print(dictionary.items())