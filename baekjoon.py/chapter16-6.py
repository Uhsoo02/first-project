import sys  # sys 모듈을 임포트하여 표준 입력을 사용할 수 있게 함
from collections import deque  # collections 모듈에서 deque를 임포트하여 큐를 사용할 수 있게 함

N = int(sys.stdin.readline())  # 입력으로 받은 첫 번째 줄의 정수를 N에 저장 (명령의 개수)
DQ = deque()  # deque 객체를 생성하여 DQ에 저장 (이 객체를 큐로 사용)

for _ in range(N):  # N번 반복하여 각 명령을 처리
    E = sys.stdin.readline().split()  # 입력으로 받은 명령을 공백을 기준으로 분리하여 E에 저장

    if E[0] == 'push':  # 명령이 'push'인 경우
        DQ.append(int(E[1]))  # E[1]에 있는 정수를 큐에 추가

    if E[0] == 'pop':  # 명령이 'pop'인 경우
        if DQ:  # 큐가 비어있지 않은 경우
            print(DQ.popleft())  # 큐의 가장 앞에 있는 정수를 제거하고 출력
        else:
            print(-1)  # 큐가 비어있는 경우 -1 출력

    if E[0] == 'size':  # 명령이 'size'인 경우
        print(len(DQ))  # 큐에 들어있는 정수의 개수를 출력

    if E[0] == 'empty':  # 명령이 'empty'인 경우
        if DQ:  # 큐가 비어있지 않은 경우
            print('0')  # 0 출력
        else:
            print('1')  # 큐가 비어있는 경우 1 출력

    if E[0] == 'front':  # 명령이 'front'인 경우
        if DQ:  # 큐가 비어있지 않은 경우
            print(DQ[0])  # 큐의 가장 앞에 있는 정수를 출력
        else:
            print(-1)  # 큐가 비어있는 경우 -1 출력

    if E[0] == 'back':  # 명령이 'back'인 경우
        if DQ:  # 큐가 비어있지 않은 경우
            print(DQ[-1])  # 큐의 가장 뒤에 있는 정수를 출력
        else:
            print(-1)  # 큐가 비어있는 경우 -1 출력
