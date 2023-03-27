from itertools import product
def solution(word):
    answer = 0
    total_list = []
    for i in range(1, 6) :
        temp = set(product("AEIOU", repeat=i))
        for t in temp :
            total_list.append("".join(t))
    total_list.sort()
    for i, w in enumerate(total_list, start=1) :
        if w==word : 
            answer = i
            break
    return answer