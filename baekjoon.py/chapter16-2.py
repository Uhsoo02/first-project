import sys

K = int(sys.stdin.readline())    # 첫 번째 줄에 정수 K가 주어진다.

ST = []             # 빈 스택 생성
sum_v = 0           # 합을 구할 sum_v 변수 초기화

for _ in range(K):  # K개의 줄에 정수가 1개씩 주어진다.
    num = int(sys.stdin.readline())  # 값 입력받기

    if ST and num == 0: # 스택에 값이 존재하고, 입력받은 값이 0이면
        ST.pop()        # 스택에서 pop()
    else:
        ST.append(num)  # 아닌경우 스택에 append()

print(sum(ST))          # 스택의 합을 출력