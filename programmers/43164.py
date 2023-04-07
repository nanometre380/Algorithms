final = []

def dfs(tickets, checked, start, dst, route) :
    global final
    if sum(checked.values()) == 0 :
        route.append(dst)
        if len(route) > len(final) :
            final = route[:]
        route.pop()
        return route
    
    for t in tickets :
        new_src, new_dst = t
        if dst == new_src and checked[new_src+new_dst] > 0 :
            checked[new_src+new_dst] -= 1
            route.append(t[0])
            dfs(tickets, checked, t[0], t[1], route)
            route.pop()
            checked[new_src+new_dst] += 1
        else :
            continue

def solution(tickets):
    checked = {}
    start = []
    tickets = sorted(tickets, key = lambda x : (x[0], x[1]))
    for i, t in enumerate(tickets) : 
        if t[0]+t[1] in checked.keys() :
            checked[t[0]+t[1]] += 1
        else :
            checked[t[0]+t[1]] = 1
        if t[0] == "ICN" :
            start.append(t)
    for t in start :
        checked[t[0]+t[1]] -= 1
        dfs(tickets, checked, t[0], t[1], [t[0]])
        checked[t[0]+t[1]] += 1
    return final


# BFS가 아니야~ DFS로 하자
"""
from collections import deque
def bfs(tickets, checked, start) :
    queue = deque()
    route = []
    queue.append(tickets[start])
    src = ""
    dst = ""
    while queue :
        src, dst = queue.popleft()
        route.append(src)
        checked[src+dst] -= 1
        for new_src, new_dst in tickets :
            if new_src == src and new_dst == dst :
                continue
            if new_src == dst and checked[new_src+new_dst] != 0:
                queue.append([new_src, new_dst])
                break
    route.append(dst)
    return route

def get_checked(tickets) :
        checked = {}
        for i, ticket in enumerate(tickets) :
            if ticket[0]+ticket[1] not in checked.keys() :
                checked[ticket[0]+ticket[1]] = 1
            else : 
                checked[ticket[0]+ticket[1]] += 1
        return checked

def solution(tickets):
    answer = []
    checked = {}
    start = []
    routes = []
    tickets = sorted(tickets, key = lambda x : (x[0], x[1]))
    
    for i, ticket in enumerate(tickets) :
        if ticket[0] == "ICN" :
            start.append(i)
    
    for i in range(len(start)) :
        checked = {}
        checked = get_checked(tickets)
        print(checked)
        temp = bfs(tickets, checked, start[i])
        if len(temp) > len(routes) :
            routes = temp
    return routes
    """