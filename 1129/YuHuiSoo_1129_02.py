# 과제2: 문자열매칭(Horspool)
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024-11-29

NO_OF_CHARS = 128
def shift_table(pat):
    m = len(pat)
    tbl = [m]*NO_OF_CHARS

    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i
    
    return tbl

def search_horspool(T, P):
    m = len(P)
    n = len(T)
    t = shift_table(P)
    i = m-1
    while(i <= n-1):
        k = 0
        while k <= m-1 and P[m-1-k] == T[i-k]:
            k += 1
        if k == m:
            return i-m+1
        else:
            i += t[ord(T[i])]
    return -1

print("패턴의 위치 :", search_horspool("APPLEMANGOBANANAGRAPE", "BANANA"))