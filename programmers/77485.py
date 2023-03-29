def make_table(rows, columns) :
    table = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    for i in range(1, rows+1) :
        for j in range(1, columns+1) :
            table[i][j] = ((i-1)*columns+j)
    return table

def rotate_table(x1, y1, x2, y2, table) :
    tmp = table[x1][y1]
    min_num = tmp
    
    for x in range(x1+1, x2+1, 1) :
        table[x-1][y1] = table[x][y1]
        min_num = min(min_num, table[x][y1])
    for y in range(y1+1, y2+1, 1) :
        table[x2][y-1] = table[x2][y]
        min_num = min(min_num, table[x2][y])
    for x in range(x2-1, x1-1, -1) :
        table[x+1][y2] = table[x][y2]
        min_num = min(min_num, table[x][y2])
    for y in range(y2-1, y1-1, -1) :
        table[x1][y+1] = table[x1][y]
        min_num = min(min_num, table[x1][y])

    table[x1][y1+1] = tmp
    return table, min_num
    
def solution(rows, columns, queries):
    table = make_table(rows, columns)
    min_num = []
    for q in queries :
        x1, y1, x2, y2 = q
        #return rotate_table(x1, y1, x2, y2, table)
        table, min_temp = rotate_table(x1, y1, x2, y2, table)
        min_num.append(min_temp)
    return min_num