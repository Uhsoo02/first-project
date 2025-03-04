from collections import deque  # collections 모듈에서 deque를 임포트하여 큐를 사용할 수 있게 함
import sys  # sys 모듈을 임포트하여 표준 입력을 사용할 수 있게 함
input = sys.stdin.readline  # 입력을 더 빠르게 받기 위해 sys.stdin.readline을 input으로 사용

N = int(input())  # 입력으로 받은 첫 번째 줄의 정수를 N에 저장 (queuestack을 구성하는 자료구조의 개수)
A = list(map(int, input().split()))  # 길이 N의 수열 A를 입력받아 리스트로 저장 (각 자료구조의 타입)
B = list(map(int, input().split()))  # 길이 N의 수열 B를 입력받아 리스트로 저장 (각 자료구조의 초기 값)
M = int(input())  # 입력으로 받은 네 번째 줄의 정수를 M에 저장 (삽입할 수열의 길이)
C = list(map(int, input().split()))  # 길이 M의 수열 C를 입력받아 리스트로 저장 (삽입할 수열)

queue = deque([])  # deque 객체를 생성하여 queue에 저장 (이 객체를 큐로 사용)
for i in range(N):  # N번 반복하여 각 자료구조를 검사
    if A[i] == 0:  # A[i]가 0인 경우 (큐인 자료구조)
        queue.append(B[i])  # B[i]의 값을 큐에 추가

# 배열 C의 원소를 1개 appendleft 할 때마다 pop 연산 수행
for i in range(M):  # M번 반복하여 각 원소를 처리
    queue.appendleft(C[i])  # C[i]의 값을 큐의 맨 앞에 추가
    print(queue.pop(), end=' ')  # 큐의 맨 뒤에 있는 값을 제거하고 출력 (공백으로 구분)
