def solution(prices):
    answer = []
    len_p = len(prices)
    for i in range(len_p) :
        temp = 0
        for j in range(i, len_p) :
            if prices[i] > prices[j] or j == len_p-1:
                answer.append(temp)
                break
            temp += 1
    return answer