def solution(clothes):
    answer = 1
    dic = {}
    for name, kind in clothes : 
        if kind in dic :
            dic[kind] += 1
        else :
            dic[kind] = 1
    for k in dic.keys() :
        answer *= (dic[k]+1)
    return answer-1