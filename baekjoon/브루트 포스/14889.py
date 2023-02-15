# N은 짝수 - 스타트팀, 링크팀으로 나누기
# 팀의 능력치 - Sij의 합
# i번 사람과 j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치 -> Sij + Sji
from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
min = 100
skill = [list(map(int, input().split())) for _ in range(n)]
cases = list(combinations([i for i in range(n)], n//2))
for case in cases :
    adv_case = set([i for i in range(n)]) - set(case)
    case_combi = combinations(case, 2)
    adv_combi = combinations(adv_case, 2)
    s1= 0
    s2 = 0
    for start, link in zip(case_combi, adv_combi) :
        s1 += skill[start[0]][start[1]] + skill[start[1]][start[0]]
        s2 += skill[link[0]][link[1]] + skill[link[1]][link[0]]
    if min > abs(s1-s2) :
        min = abs(s1-s2)

print(min)
    