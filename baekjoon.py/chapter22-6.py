# 비트마스크 사용을 위한 전역 변수
rows = [0] * 9
cols = [0] * 9
blocks = [[0] * 3 for _ in range(3)]
zero_point = []

def set_mask(n, m, num, flag):
    """ 비트마스크로 숫자를 기록하거나 해제하는 함수 """
    bit = 1 << num
    if flag:
        rows[n] |= bit
        cols[m] |= bit
        blocks[n // 3][m // 3] |= bit
    else:
        rows[n] &= ~bit
        cols[m] &= ~bit
        blocks[n // 3][m // 3] &= ~bit

def check_mask(n, m, num):
    """ 비트마스크로 숫자가 사용 가능한지 확인하는 함수 """
    bit = 1 << num
    return not (rows[n] & bit or cols[m] & bit or blocks[n // 3][m // 3] & bit)

def bt(index):
    global answer_flag
    if answer_flag:
        return

    if index == len(zero_point):
        for line in sdoku:
            print(*line)
        answer_flag = True
        return

    i, j = zero_point[index]
    for num in range(9):
        if check_mask(i, j, num):
            # num이 해당 칸에 들어갈 수 있으면 배치
            set_mask(i, j, num, True)
            sdoku[i][j] = num + 1
            bt(index + 1)
            if answer_flag:
                return
            # 백트래킹: 다시 0으로 되돌리고 마스크 해제
            set_mask(i, j, num, False)
            sdoku[i][j] = 0

# 입력 받기
sdoku = []
for i in range(9):
    row = list(map(int, input().split()))
    sdoku.append(row)
    for j in range(9):
        if row[j] != 0:
            set_mask(i, j, row[j] - 1, True)
        else:
            zero_point.append((i, j))

answer_flag = False
bt(0)
