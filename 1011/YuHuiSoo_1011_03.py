# 과제3: 순차 탐색 억지기법,  강의노트[4] p.41
# 이름: 유희수
# 날짜: 2024.10.11

def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i+1
    return -1

A = [32, 14, 5, 17, 23, 9, 11, 4, 26, 29]

print(f"리스트 A: {A}")
print(f"리스트 A 크기: {len(A)}")
num = int(input("찾고자 하는 수 입력: "))
print(f"순차 탐색 횟수: {sequential_search(A, num)}")