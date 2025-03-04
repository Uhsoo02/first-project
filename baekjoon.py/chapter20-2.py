from sys import stdin

# 입력을 빠르게 받기 위해 stdin.readline을 사용
input = stdin.readline

# 사용자 입력 횟수 n을 입력받음
n = int(input())

# 고무오리 놀이에 참여한 사용자를 저장할 집합 gom
gom = set()

# 고무오리 놀이에 참여한 사용자 수를 저장할 변수 cnt
cnt = 0

# n번 반복하며 사용자 입력을 받음
for _ in range(n):
    # 사용자 입력을 받고 양쪽 공백을 제거
    user = input().strip()
    
    # 입력이 'ENTER'인 경우
    if user == 'ENTER':
        # 현재까지 참여한 사용자 수를 cnt에 더함
        cnt += len(gom)
        # 새로운 라운드를 시작하므로 gom을 초기화
        gom = set()
    else:
        # 사용자 이름을 gom 집합에 추가
        gom.add(user)

# 마지막 라운드에 참여한 사용자 수를 cnt에 더함
cnt += len(gom)

# 최종 참여한 사용자 수 출력
print(cnt)
