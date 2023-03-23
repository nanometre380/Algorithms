import sys
input = sys.stdin.readline

def longest_arr() :
    for i in range(1, len(arr)) :
        max_dp = 0
        for j in range(0, i) :
            if arr[j] < arr[i] :
                max_dp = max(max_dp, dp[j])
            dp[i] = max_dp+1

n = int(input())
arr = list(map(int, input().split()))
dp = [1]*n
longest_arr()
print(max(dp))