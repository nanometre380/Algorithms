from collections import deque
from collections import Counter

def solution(topping):
    answer = 0
    left = set()
    right = deque(topping)
    right_count = Counter(topping)
    while len(right) == 0 :
        temp = right.popleft()
        left.add(temp)
        right_count[temp] -= 1
        print(left)
        print(right)
        print(right_count)
        if right_count[temp] == 0 :
            right_count.pop(temp)
        if len(left) == len(right_count) :
            answer += 1
    return answer

topping = [1, 2, 1, 3, 1, 4, 1, 2]
print(solution(topping))