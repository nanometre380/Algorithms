def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1) :
        if yellow%i == 0 : 
            yellow_y = yellow//i
            yellow_x = i
        if (yellow_x+2)*2 + (yellow_y)*2 == brown : 
            answer.extend([yellow_y+2, yellow_x+2])
            break
    return answer

# for문 하나로도 풀 수 있음!