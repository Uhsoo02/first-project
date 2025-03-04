import sys

# 입력받을 단어의 개수 n과 최소 길이 m을 입력받음
n, m = map(int, input().split())

# 단어와 그 빈도를 저장할 딕셔너리 note 초기화
note = dict()

# n번 반복하며 단어를 입력받음
for _ in range(n):
    # 단어를 입력받고 양쪽 공백을 제거
    s = sys.stdin.readline().strip()
    
    # 단어의 길이가 m 이상인 경우에만 처리
    if len(s) >= m:
        # 이미 딕셔너리에 있는 단어라면 빈도 증가
        if s in note:
            note[s] += 1
        # 딕셔너리에 없는 단어라면 새로 추가
        else:
            note[s] = 1

# 딕셔너리를 정렬
# 정렬 기준: 빈도 내림차순, 길이 내림차순, 사전 순 오름차순
note = sorted(note.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# 정렬된 단어들을 출력
for i in note:
    print(i[0])
