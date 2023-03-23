import sys
input = sys.stdin.readline

def get_score() :
    if n == 1 :
        dp[-1] = stair[0] 
        return 
    elif n == 2 :
        dp[-1] = stair[1] + stair[0]
        return
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[1]+stair[2], stair[0]+stair[2])
    for i in range(3, n) :
        dp[i] = max(dp[i-2], dp[i-3]+stair[i-1])+stair[i]
    return

n = int(input())
stair = []
dp = [0]*n
for _ in range(n):
    stair.append(int(input()))

get_score()
print(dp[-1])