import sys
input = sys.stdin.readline

def get_dp() :
    if n == 1 :
        return 0
    if n <= 3 : 
        return 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1) :
        div3, div2, min1 = INF, INF, INF
        if i%3 == 0 :
            div3 = dp[i//3]
        if i%2 == 0 :
            div2 = dp[i//2]
        min1 = dp[i-1]
        dp[i] = min(div3, div2, min1)+1
    return dp[n]

INF = float('inf')
n = int(input())
dp = [0 for _ in range(n+1)]
print(get_dp())
