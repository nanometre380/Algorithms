import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
while True : 
    if n%5 == 0 :
        cnt += n//5
        n %= 5
    else : 
        n -= 3
        cnt += 1
    if n == 0 : 
        print(cnt)
        break
    elif n < 0 :
        print(-1)
        break