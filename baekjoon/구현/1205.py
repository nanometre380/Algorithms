# 등수 구하기
# 노래마다 랭킹리스트 - 등수는 위에서부터 몇 번째 점수인지/같은 점수가 있을 땐 점수의 등수 중 가장 작은 등수
# 랭킹 리스트에 올라갈 수 있는 점수의 개수 P
# 점수 N개가 내림차순으로 주어짐 + 새로운 점수
# 새로운 점수가 몇 등하는지
# 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1

import sys
input = sys.stdin.readline

def get_rank(new, scores, p) :
    cnt = 0
    before_rank = 1
    for i, score in enumerate(scores) : 
        if cnt == p :
            return -1
        if new > score :
            if scores[i-1] == new : 
                return before_rank
            else :
                return cnt+1
        cnt += 1
        if i >= 1 and scores[i-1] != score :
            before_rank = cnt
    if cnt < p :
        if scores[-1] == new : 
            return before_rank
        else :
            return cnt+1
    return -1
    
n, new_score, p = map(int, input().split())
if n != 0 :
    scores = list(map(int, input().split()))
    print(get_rank(new_score, scores, p))
else :
    print(1)
