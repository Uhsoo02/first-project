def solve_n_queens(n, col, left_diag, right_diag):
    if col == (1 << n) - 1:  # 모든 열에 퀸이 배치되었을 경우
        return 1
    count = 0
    possible_positions = (~(col | left_diag | right_diag)) & ((1 << n) - 1)  # 가능한 위치 계산
    while possible_positions:
        position = possible_positions & -possible_positions  # 가장 오른쪽 비트를 가져오기
        possible_positions -= position  # 퀸을 놓을 수 있는 위치에서 제거
        count += solve_n_queens(n, col | position, (left_diag | position) << 1, (right_diag | position) >> 1)
    return count

def n_queens(n):
    return solve_n_queens(n, 0, 0, 0)

# 입력
N = int(input())
# 출력
print(n_queens(N))
