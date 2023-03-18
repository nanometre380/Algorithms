# 외판원 순회 문제
import sys
input = sys.stdin.readline

def get_routine(start, cnt, cost) :
    global min_cost
    if cost > min_cost :
        return
    if cnt == n-1 :
        if w[start][0] != 0 :
            min_cost = min(min_cost, cost+w[start][0])
        return
    for i in range(1, n) :
        if check[i] == False and w[start][i] != 0 : 
            check[i] = True
            get_routine(i, cnt+1, cost+w[start][i])
            check[i] = False


n = int(input())

w = [list(map(int, input().split())) for _ in range(n)]
min_cost = 10**8
check = [False for _ in range(n)]
get_routine(0, 0, 0)
print(min_cost)
