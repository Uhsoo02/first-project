# 병합 정렬 함수: A[p ~ r]을 오름차순 정렬한다.
def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2  # q는 p, r의 중간 지점
        merge_sort(A, p, q)       # 전반부 정렬
        merge_sort(A, q + 1, r)   # 후반부 정렬
        merge(A, p, q, r)         # 병합

# A[p~q]와 A[(q+1)~r]을 병합하여 A[p~r]을 오름차순 정렬된 상태로 만든다.
# A[p~q]와 A[(q+1)~r]은 이미 오름차순으로 정렬되어 있다.
def merge(A, p, q, r):
    global cnt, res  # cnt와 res는 전역 변수로 사용
    i = p  # 왼쪽 배열의 시작 인덱스
    j = q + 1  # 오른쪽 배열의 시작 인덱스
    tmp = []  # 임시 배열
    
    # 왼쪽과 오른쪽 배열을 비교하며 작은 값을 tmp에 추가
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    # 왼쪽 배열 부분이 남은 경우
    while i <= q:
        tmp.append(A[i])
        i += 1
    
    # 오른쪽 배열 부분이 남은 경우
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    i = p
    t = 0
    
    # 임시 배열의 값을 원래 배열 A에 복사
    while i <= r:
        A[i] = tmp[t]
        cnt += 1  # 병합 횟수 증가
        if cnt == K:  # 병합 횟수가 K와 같으면 결과 저장
            res = A[i]
            break
        i += 1
        t += 1

# 사용자로부터 N과 K를 입력받음
N, K = map(int, input().split())
# 사용자로부터 정렬할 배열 A를 입력받음
A = list(map(int, input().split()))
# 병합 횟수를 저장할 변수 cnt 초기화
cnt = 0
# 결과를 저장할 변수 res 초기화
res = -1
# 병합 정렬 실행
merge_sort(A, 0, N - 1)
# 결과 출력
print(res)
