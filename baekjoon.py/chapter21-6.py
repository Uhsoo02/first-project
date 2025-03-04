# 별 찍기 함수: n x n 크기의 별 패턴을 생성
def draw_stars(n):
    # 기저 조건: n이 1일 때, 별 하나를 반환
    if n == 1:
        return ['*']

    # 재귀 호출: n을 3으로 나눈 값에 대해 별 패턴을 생성
    Stars = draw_stars(n // 3)
    lst = []  # 결과를 저장할 리스트

    # 첫 번째 부분: 각 줄을 3배로 확장
    for star in Stars:
        lst.append(star * 3)
    # 두 번째 부분: 각 줄 사이에 (n // 3) 만큼의 공백을 추가
    for star in Stars:
        lst.append(star + ' ' * (n // 3) + star)
    # 세 번째 부분: 각 줄을 3배로 확장
    for star in Stars:
        lst.append(star * 3)

    # 생성된 별 패턴 리스트를 반환
    return lst

# 사용자로부터 정수 N을 입력받음
N = int(input())
# 별 패턴을 생성하고, 각 줄을 줄바꿈으로 연결하여 출력
print('\n'.join(draw_stars(N)))
