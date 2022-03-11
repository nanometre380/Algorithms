import math

def min_move(x, y) :
    dist = y - x
    cnt = 0
    if dist <= 3 :
        cnt = dist
    else : 
        n = int(math.sqrt(dist))
        if dist == n**2 :
            cnt = 2*n-1
        elif dist > n**2 and dist <= n**2 + n :
            cnt = 2*n
        elif dist > n**2 + n and dist <= (n+1)**2 :
            cnt = 2*n+1
    return cnt
    
        


t = int(input())

for i in range(t) :
    x, y = map(int, input().split())
    result = min_move(x, y)
    print(result)
