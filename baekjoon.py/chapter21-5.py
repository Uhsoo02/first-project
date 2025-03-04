# sys 모듈의 stdin을 사용하여 입력을 받음
from sys import stdin

# 입력을 빠르게 받기 위해 stdin.readline을 input으로 사용
input = stdin.readline

# 칸토어 집합을 생성하는 재귀 함수
def cantor(n):
    # 기저 조건: n이 1일 때, "-"를 반환
    if n == 1:
        return "-"
    
    # 재귀 호출: n을 3으로 나눈 값에 대해 칸토어 집합을 생성
    cantor_unit = cantor(n // 3)
    # 중간에 (n // 3) 만큼의 공백을 추가하여 칸토어 집합을 구성
    cantor_res = cantor_unit + " " * (n // 3) + cantor_unit

    # 구성된 칸토어 집합을 반환
    return cantor_res

# 무한 루프를 통해 사용자 입력을 받음
while True:
    try:
        # 사용자로부터 정수 N을 입력받음
        N = int(input())
        # 3^N 크기의 칸토어 집합을 생성하여 출력
        print(cantor(3**N))
    except:
        # 예외가 발생하면 루프를 종료
        break
