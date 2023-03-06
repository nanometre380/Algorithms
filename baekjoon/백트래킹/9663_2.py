import sys
input = sys.stdin.readline

n = int(input())
ans = 0
check_col = [False for _ in range(15)]
check_right = [False for _ in range(30)]
check_left = [False for _ in range(30)]

def count_queens(row) :
    global ans
    if row == n :
        ans += 1
        return
    for i in range(n) :
        if check_col[i] or check_right[row-i+n] or check_left[row+i] :
            continue
        check_col[i] = True
        check_right[row-i+n] = True
        check_left[row+i] = True
        count_queens(row+1)
        check_col[i] = False
        check_right[row-i+n] = False
        check_left[row+i] = False

count_queens(0)
print(ans)
