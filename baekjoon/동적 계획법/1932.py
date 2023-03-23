# 정수 삼각형
import sys
input = sys.stdin.readline

def get_max() :
    dp[1][1] = tri[1][1]
    for i in range(2, n+1) :
        for j in range(1, i+1) :
            dp[i][j] = max(dp[i-1][j] + tri[i][j], dp[i-1][j-1] + tri[i][j])

n = int(input())
tri = [[0]]
for _ in range(n) :
    tri.append([0]+list(map(int, input().split()))+[0])
dp = [[0]*(n+1) for _ in range(n+1)]
get_max()
print(max(dp[n]))


