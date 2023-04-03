def solution(land) :
    answer = 0
    for i in range(1, len(land)) :
        for j in range(4) :
            land[i][j] = max(land[i-1][:j] + land[i-1][j+1]) + land[i][j]
    answer = max(len(land)-1)
    return answer
land = [[1,2,3,4]]
solution(land)

"""
def solution(land):
    answer = 0
    len_land = len(land)
    def get_max(i, j) :
        max_value = 0
        for k in range(4) :
            if k == j :
                continue
            max_value = max(max_value, land[i-1][k])
        return max_value
    
    def game() :
        for i in range(1, len_land) :
            for j in range(4) :
                land[i][j] += get_max(i, j)
        return max(land[len_land-1])
    
    answer = game()
    return answer
"""