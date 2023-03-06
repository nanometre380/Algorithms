import sys
input = sys.stdin.readline

n, new_score, p = map(int, input().split())

if n == 0 :
    answer = 1
else : 
    scores = list(map(int, input().split()))
    scores.append(new_score)
    scores.sort(reverse=True)
    first_idx = scores.index(new_score)
    same_score = scores.count(new_score)
    if first_idx + same_score > p :
        answer = -1
    else :
        answer = first_idx+1
    
print(answer)