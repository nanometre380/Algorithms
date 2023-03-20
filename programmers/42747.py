def solution(citations) :
    citations.sort()
    l = len(citations)
    for i in range(l) :
        if citations[i] >= l-i :
            return l-i
    return 0

# def solution(citations):
#     answer = 0
#     citations.sort(reverse=True)
#     h = citations[0]
#     for h in range(citations[0], 0, -1):
#         cnt_up = 0
#         for c in citations : 
#             if c >= h :
#                 cnt_up += 1
#         if cnt_up >= h :
#             answer = h
#             break
#     return answer