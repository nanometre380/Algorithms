def solution(board):
    r = len(board)
    c = len(board[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    dp[0] = board[0]
    max_v = 0
    for i in range(r) :
        dp[i][0] = board[i][0]
    
    for i in range(1, r) :
        for j in range(1, c) :
            if board[i][j] == 1 :
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
    for i in range(r) :
        max_v = max(max_v, *dp[i])
    return max_v**2