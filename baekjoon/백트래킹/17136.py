import sys
input = sys.stdin.readline

def promising(x, y, size) :
    for i in range(x, x+size, 1):
        for j in range(y, y+size, 1):
            if arr[i][j] != 1:
                return False
    return True

def fill_box(x, y, size, c) :
    for i in range(x, x+size, 1) :
        for j in range(y, y+size, 1) :
            arr[i][j] = c

def backtracking(idx, cnt) :
    global answer
    x = idx//10 #행
    y = idx%10  #열
    if idx == 100 :
        answer = min(answer, cnt)
        return
    if arr[x][y] == 0 :
        backtracking(idx+1, cnt)
        return
    for i in range(5, 0, -1) :
        if x+i > 10 or y+i > 10 : 
            continue
        if promising(x, y, i) and papers[i-1] > 0 :
            papers[i-1] -= 1
            fill_box(x, y, i, 0)
            backtracking(idx+i, cnt+1)
            papers[i-1] += 1
            fill_box(x, y, i, 1)
    return
    

arr = [list(map(int, input().split())) for _ in range(10)]
answer = 100
papers = [5 for _ in range(5)]
backtracking(0, 0)
if answer == 100 :
    print(-1)
else : 
    print(answer)