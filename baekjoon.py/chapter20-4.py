import sys
input = sys.stdin.readline

# 입력받을 숫자의 개수 n을 입력받음
n = int(input())

# n개의 숫자를 입력받아 리스트 lst에 저장
lst = [int(input()) for i in range(n)]

# 산술평균 계산 및 출력
# sum(lst)는 리스트의 모든 요소의 합, n은 요소의 개수
# round 함수를 사용하여 반올림한 값을 출력
print(round(sum(lst) / n))

# 리스트를 오름차순으로 정렬
lst.sort()

# 중앙값 계산 및 출력
# n//2는 리스트의 중간 인덱스를 나타냄
print(lst[n // 2])

# 각 숫자의 빈도를 저장할 딕셔너리 cnt 초기화
cnt = dict()

# 리스트의 각 숫자에 대해 빈도를 계산
for i in lst:
    if i in cnt:
        cnt[i] += 1  # 이미 딕셔너리에 있는 경우 빈도 증가
    else:
        cnt[i] = 1   # 딕셔너리에 없는 경우 새로 추가

# 최대 빈도를 찾음
mx = max(cnt.values())

# 최대 빈도를 가진 숫자들을 저장할 리스트 mx_lst 초기화
mx_lst = []

# 최대 빈도를 가진 숫자들을 mx_lst에 추가
for i in cnt:
    if cnt[i] == mx:
        mx_lst.append(i)

# 최빈값 출력
# 최빈값이 하나라면 그 값을 출력, 여러 개라면 두 번째로 작은 값을 출력
print(mx_lst[0]) if len(mx_lst) == 1 else print(mx_lst[1])

# 범위 계산 및 출력
# max(lst)는 리스트의 최댓값, min(lst)는 리스트의 최솟값
print(max(lst) - min(lst))
