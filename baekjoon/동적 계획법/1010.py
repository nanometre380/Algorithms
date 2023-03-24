import sys
input = sys.stdin.readline

MAX = 30
def get_cases() :
    for i in range(2, MAX+1) :
        for j in range(1, MAX+1) :
            if j < i :
                dp[i][j] = 0
            else : 
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

dp = [[0]*(MAX+1) for _ in range(MAX+1)]
dp[1] = [i for i in range(0, MAX+1)]
get_cases()
num = int(input())
for _ in range(num) : 
    n,m = map(int, input().split())
    print(dp[n][m])