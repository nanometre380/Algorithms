def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    print(routes)
    camera = -float('inf')
    for i in range(len(routes)) :
        c_in, c_out = routes[i]
        if camera < c_in :
            answer += 1
            camera = c_out
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))