# 블랙잭
# 합이 21을 넘지 않는 한도에서 합을 크게 만들기
# 카드에 써져있는 숫자가 주어졌을 때 M에 최대한 가까운 카드 3장의 합

import sys
from itertools import combinations
input = sys.stdin.readline

n, max = map(int, input().split())
diff = max
cards = list(map(int, input().split()))
cases = combinations(cards, 3)
ans = 0

for case in cases : 
    total = sum(case)
    if total <= max and (max-total) < diff :
        diff = max-total
        ans = total

print(ans)