from collections import deque

def solution(order):
    order = deque(order)
    line1 = deque(i for i in range(order[0], len(order)+1))
    line2 = [i for i in range(1, order[0])]
    print(line1)
    print(line2)
    cnt = 0
    flag = True
    while flag and order :
        cur = order.popleft()
        while True :
            if line1 and line1[0] == cur:
                line1.popleft()
                cnt+=1
                break
            if line2 and line2[-1] == cur:
                line2.pop()
                cnt+=1
                break
            if not line1 :
                flag = False
                break
            else:
                line2.append(line1.popleft())
    
    return cnt

print(solution([4,3,1,2,5]))