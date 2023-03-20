def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    l = len(citations)
    for i in range(l):
        if citations[i] <= i+1 :
            answer = i+1
            break
    return answer

print(solution([3, 0, 6, 1, 5]))