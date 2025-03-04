# 과제2: 편집거리
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024-11-22

def edit_distance(S, T, m, n):
    if m == 0: return n                 # S가 공백이면, T의 모든 문자를 S에 삽입
    if n == 0: return m                 # T가 공백이면, S의 모든 문자들을 삭제

    if S[m-1] == T[n-1]:                # 마지막 문자가 같으면, 이 문자들 무시
        return edit_distance(S, T, m-1, n-1)
    
    # 만약 그렇지 않으면, 세 연산을 모두 적용해 봄
    return 1 + min( edit_distance(S, T, m, n-1),    # 삽입
                    edit_distance(S, T, m-1, n),    # 삭제
                    edit_distance(S, T, m-1, n-1))  # 대체

def edit_distance_mem(S, T, m, n, mem):
    if m == 0: return n
    if n == 0: return m

    if mem[m-1][n-1] == None:
        if S[m-1] == T[n-1]:
            mem[m-1][n-1] = edit_distance_mem(S, T, m-1, n-1, mem)
        
        else:   # 그렇지 않으면, 세 연산을 모두 적용한다.
            mem[m-1][n-1] = 1 + \
            min( edit_distance_mem(S, T, m, n-1, mem),
                 edit_distance_mem(S, T, m-1, n, mem),
                 edit_distance_mem(S, T, m-1, n-1, mem))
        print("mem[%d][%d] = "%(m-1,n-1), mem[m-1][n-1])
    
    return mem[m-1][n-1]

S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)
print("문자열: ", S, T)
print("편집거리(분할정복    )= ", edit_distance(S, T, m, n))

mem = [[None for _ in range(n)] for _ in range(m)]
dist = edit_distance_mem(S, T, m, n, mem)
print("편집거리(메모이제이션)= ", edit_distance_mem(S, T, m, n, mem))