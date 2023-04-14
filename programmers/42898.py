def solution(m, n, puddles): #동젹계획법 - 격자판에서 오른쪽과 아래쪽으로만 움직일 때 최단경로는 DP로 구할 수 있음. 
    # m이 가로, n이 세로
    answer = 0
    dp = [[1 for i in range(m+1)] for j in range(n+1)]
    for p in puddles :
        if len(p) == 0 :
            continue
        else : 
            x, y = p
            dp[y][x] = 0
    temp = 1
    for i in range(m+1) :
        if dp[1][i] != 0 :
            dp[1][i] = temp
        elif dp[1][i] == 0 :
            temp = 0
    temp = 1
    for j in range(n+1) :
        if dp[j][1] != 0 :
            dp[j][1] = temp
        elif dp[j][1] == 0 :
            temp = 0
    
    dp[n][m] = 0
    
    for i in range(2, n+1) :
        for j in range(2, m+1) :
            if dp[i][j] == 0 and (i!=n or j!=m) :
                continue
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[n][m]%1000000007