import sys
input = sys.stdin.readline

rev_order = []
for i in range(10) :
    rev_order.append(list(map(int, input().split())))

cards = [_ for _ in range(1, 21)]

for i in range(10) :
    reverse_temp =cards[rev_order[i][0]-1:rev_order[i][1]]
    reverse_temp = reverse_temp[::-1]
    cards[rev_order[i][0]-1:rev_order[i][1]] = reverse_temp

print(*cards)
