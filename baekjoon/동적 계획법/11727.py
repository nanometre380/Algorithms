import sys
input = sys.stdin.readline

def fill_tiles() :
    dp[1] = 1
    if n == 1 :
        return
    dp[2] = 3
    for i in range(3, n+1) :
        dp[i] = dp[i-1] + dp[i-2]*2
        dp[i] %= 10007

n = int(input())
dp = [0 for _ in range(n+1)]
fill_tiles()
print(dp[n]%10007)