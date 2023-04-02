min_case = float('inf')
max_r, max_c = 0, 0
check = []

def set_xy(maps) :
    global max_r, max_c
    max_r = len(maps)
    max_c = len(maps[0])
    for _ in range(max_r) :
        check.append([False for _ in range(max_c)])

def get_route(maps, cnt, i, j) :
    global min_case
    if i == max_r-1 and j == max_c-1 :
        min_case = min(min_case, cnt)
    if maps[i][j] == 0 :
        return
    if i <= max_r-2 and check[i+1][j] != True :
        check[i+1][j] = True
        get_route(maps, cnt+1, i+1, j)
        check[i+1][j] = False
    if j <= max_c-2 and check[i][j+1] != True :
        check[i][j+1] = True
        get_route(maps, cnt+1, i, j+1)
        check[i][j+1] = False
    if i >= 1 and check[i-1][j] != True: 
        check[i-1][j] = True
        get_route(maps, cnt+1, i-1, j)
        check[i-1][j] = False
    if j >= 1 and check[i][j-1] != True :
        check[i][j-1] = True
        get_route(maps, cnt+1, i, j-1)
        check[i][j-1] = False
    
def solution(maps):
    global min_case
    set_xy(maps)
    get_route(maps, 1, 0, 0)
    if min_case == float('inf') :
        min_case = -1
    return min_case