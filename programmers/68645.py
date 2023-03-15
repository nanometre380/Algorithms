def solution(n):
    answer = []
    temp_arr = [[0 for _ in range(0, i+1)] for i in range(n)]
    value = 0
    row_v = -1
    col_v = 0
    for i in range(n, 0, -3) :
        temp_i = i
        for j in range(0, temp_i) :
            value += 1
            row_v += 1
            temp_arr[row_v][col_v] = value 
        for j in range(0, temp_i-1) :
            value += 1
            col_v += 1
            temp_arr[row_v][col_v] = value
        for j in range(0, temp_i-2) :
            row_v -= 1
            col_v -= 1
            value += 1
            temp_arr[row_v][col_v] = value
    
    print(temp_arr)
    return answer

n = 6
solution(n)