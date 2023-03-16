# 외판원 순회 문제 - 아직
import sys
input = sys.stdin.readline

def get_routine(start, end, cnt) :
    if cnt == n :
        if w[end][start] != 0 :
            print(min_cost + w[end][start])
        return
    

n = int(input())

w = [list(map(int, input().split())) for _ in range(n)]
min_cost = 0
