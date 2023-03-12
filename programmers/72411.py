from itertools import combinations

def get_course(orders, n) :
    cnt = {}
    for order in orders : 
        cases = combinations(order, n)
        for c in cases : 
            c = list(c)
            c = sorted(c)
            key = "".join(c)
            if key in cnt : 
                cnt[key] += 1
            else : 
                cnt[key] = 1
    if len(cnt) == 0 :
        return []
    cnt = sorted(cnt.items(), key = lambda x : -x[1])
    #print("CHECK", cnt)
    max_v = cnt[0][1]
    if max_v == 1 :
        return []
    #print(max_v)
 
    ans = []
    for c in cnt : 
        if max_v != c[1] :
            break
        if max_v == c[1] :
            ans.append(c[0]) 
    #print(ans)
    return ans


def solution(orders, course):
    answer = []
    for i in course :
        answer.extend(get_course(orders, i))
    answer.sort()
    return answer

orders= ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
print(solution(orders, course))