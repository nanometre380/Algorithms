# 백트래킹도 가능할 거 같으니까 백트래킹으로도 풀어보기

from itertools import permutations

def solution(k, dungeons):
    cases = permutations(dungeons, len(dungeons))
    max_count = 0
    for case in cases : 
        cnt = 0
        p = k
        for c in case :
            if p >= c[0] :
                p -= c[1]
                cnt += 1
            else : 
                break
        max_count = max(max_count, cnt)
    return max_count
    