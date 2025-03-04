# 사용자로부터 정수 N을 입력받음
N = int(input())

# 재귀 함수: 문자열 s가 팰린드롬인지 확인하고, 재귀 호출 횟수를 반환
def recursion(s, left, right, cnt):
    # 재귀 호출 횟수를 1 증가
    cnt += 1
    # 왼쪽 인덱스가 오른쪽 인덱스보다 크거나 같으면 팰린드롬
    if left >= right:
        return 1, cnt
    # 왼쪽과 오른쪽 문자가 다르면 팰린드롬이 아님
    elif s[left] != s[right]:
        return 0, cnt
    # 그렇지 않으면 다음 문자 쌍을 확인하기 위해 재귀 호출
    else:
        return recursion(s, left+1, right-1, cnt)

# 팰린드롬 여부를 확인하는 함수
def isPalindrome(s):
    # 재귀 호출 횟수를 0으로 초기화
    cnt = 0
    # 재귀 함수를 호출하여 팰린드롬 여부와 호출 횟수를 반환
    return recursion(s, 0, len(s)-1, cnt)

# N번 반복하며 각 입력에 대해 팰린드롬 여부와 재귀 호출 횟수를 출력
for i in range(N):
    # 사용자로부터 문자열을 입력받고, 팰린드롬 여부와 호출 횟수를 출력
    print(*isPalindrome(input()))
