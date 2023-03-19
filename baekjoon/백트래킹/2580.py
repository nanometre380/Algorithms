# 스도쿠
# 가로줄과 세로줄에는 1부터 9까지의 숫자가 한번씩만 나타나야 함
# 굵은 선으로 구분되어 있는 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 함
import sys
input = sys.stdin.readline

ROW = 9
check_row = [[False] * 10 for _ in range(10)] 
check_col = [[False] * 10 for _ in range(10)] 
check_box = [[False] * 10 for _ in range(10)] 

def pre_check() :
    for i in range(9) :
        for j in range(9) :
            if board[i][j] == 0 :
                continue
            check_row[i][board[i][j]] = True
            check_col[j][board[i][j]] = True
            check_box[(i//3)*3+(j//3)][board[i][j]] = True

def make_sudoku(cnt) :
    if cnt == ROW*ROW :
        return True
    x = cnt//9
    y = cnt%9
    if board[x][y] > 0 :
        return make_sudoku(cnt+1)
    for i in range(1, 10) :
        if check_row[x][i] or check_col[y][i] or check_box[(x//3)*3+(y//3)][i] :
            continue
        board[x][y] = i
        check_row[x][i] = True
        check_col[y][i] = True
        check_box[(x//3)*3+(y//3)][i] = True
        if make_sudoku(cnt+1) :
            return True
        board[x][y] = 0
        check_row[x][i] = False
        check_col[y][i] = False
        check_box[(x//3)*3+(y//3)][i] = False
    return False

board = [list(map(int, input().split())) for _ in range(9)]

pre_check()
make_sudoku(0)

for line in board : 
    print(*line)