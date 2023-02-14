import sys
input = sys.stdin.readline

n = int(input())
title = 666
cnt = 0
i = 0
while True :
    if "666" in str(title+i) :
        cnt += 1
        if cnt == n :
            print(title+i)
            break
    i += 1