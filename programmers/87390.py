def solution(n, left, right):
    twod = []
    start_y = left//n # 시작이 몇 번째 행인지
    start_x = left%n # 몇 번째 열인지
    end_y = right//n # 끝이 몇 번째 행인지
    
    for i in range(start_y+1, end_y+2) :
        twod.extend([i]*i)
        twod.extend([j for j in range(i+1, n+1)])
    end = right-left+1
    return twod[start_x:start_x+end]


n, left, right = 3, 2, 5
print(solution(n, left, right))