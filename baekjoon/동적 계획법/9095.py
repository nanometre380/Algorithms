import sys
input = sys.stdin.readline

def get_cases() :
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, 11) : 
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

n = int(input())
dp = [0 for _ in range(11)]
get_cases()
for _ in range(n) :
    case = int(input())
    print(dp[case])
