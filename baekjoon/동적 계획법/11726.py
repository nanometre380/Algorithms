import sys
input = sys.stdin.readline

def fill_2n() :
    if n == 1 :
        return 1
    if n == 2 : 
        return 2
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1) :
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 10007
    return dp[n]

n = int(input())
dp = [0 for i in range(n+1)]
print(fill_2n())