from collections import deque

# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
#     queue = deque(people)
#     sum_ = 0
#     while queue : 
#         max_ = queue.popleft()
#         sum_ = max_
#         while queue :
#             if sum_ + queue[-1] <= limit :
#                 sum_ += queue[-1]
#                 queue.pop()
#             else : 
#                 answer += 1
#                 break
#     return answer+1
# 최대 두명씩밖에 못 탄다고 언급 되어 있음 -> 투포인터 써라