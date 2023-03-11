from collections import Counter

def solution(k, tangerine):
    count_t = Counter(tangerine).most_common()
    sum = 0
    answer = 0
    for size, cnt in count_t :
        sum += cnt
        answer += 1
        if k <= sum :
            break
    return answer