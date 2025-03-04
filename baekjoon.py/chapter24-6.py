# 체스판 패턴에 맞지 않는 부분을 미리 계산하여 기록하는 함수
def preprocess_mismatch(board, N, M):
    # 두 가지 패턴에 대해 각각 mismatch 배열을 생성
    mismatch_W = [[0] * (M + 1) for _ in range(N + 1)]
    mismatch_B = [[0] * (M + 1) for _ in range(N + 1)]
    
    for i in range(N):
        for j in range(M):
            expected_W = 'W' if (i + j) % 2 == 0 else 'B'  # 체스판 패턴 1 (W 시작)
            expected_B = 'B' if (i + j) % 2 == 0 else 'W'  # 체스판 패턴 2 (B 시작)
            
            # 누적합을 위해 이전 값에 현재 mismatch 여부를 더해줌
            mismatch_W[i + 1][j + 1] = mismatch_W[i][j + 1] + mismatch_W[i + 1][j] - mismatch_W[i][j] + (board[i][j] != expected_W)
            mismatch_B[i + 1][j + 1] = mismatch_B[i][j + 1] + mismatch_B[i + 1][j] - mismatch_B[i][j] + (board[i][j] != expected_B)
    
    return mismatch_W, mismatch_B

# (x1, y1)에서 (x2, y2)까지의 부분 보드에서 mismatch 개수를 계산하는 함수
def count_mismatch(mismatch, x1, y1, x2, y2):
    return (mismatch[x2 + 1][y2 + 1] - mismatch[x1][y2 + 1]
            - mismatch[x2 + 1][y1] + mismatch[x1][y1])

# 전체 보드에서 최소 다시 칠해야 하는 칸 수를 찾는 함수
def min_repaints_to_chessboard(board, N, M, K):
    # 체스판 패턴에 맞지 않는 칸을 미리 계산
    mismatch_W, mismatch_B = preprocess_mismatch(board, N, M)
    
    min_repaints = float('inf')  # 매우 큰 값으로 초기화
    
    # KxK 크기로 자를 수 있는 모든 위치를 순회
    for i in range(N - K + 1):
        for j in range(M - K + 1):
            # (i, j)에서 시작하는 KxK 부분에서의 mismatch 개수 계산
            repaints_W = count_mismatch(mismatch_W, i, j, i + K - 1, j + K - 1)
            repaints_B = count_mismatch(mismatch_B, i, j, i + K - 1, j + K - 1)
            # 두 패턴 중 더 적게 다시 칠해야 하는 값 선택
            min_repaints = min(min_repaints, repaints_W, repaints_B)
    
    return min
