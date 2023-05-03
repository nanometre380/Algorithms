from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    wait = deque(truck_weights)
    bridge_sum = 0
    i = 0
    while True :
        if not bridge and not wait :
            answer = i
            break
        if bridge and bridge[0][1] == bridge_length:
            bridge_sum -= bridge.popleft()[0]
        if wait : 
            temp = wait[0]
            if temp+bridge_sum <= weight and len(bridge)+1<=bridge_length :
                bridge.append([temp, 0])
                bridge_sum += temp
                wait.popleft()
        for j in range(len(bridge)) :
            bridge[j][1] += 1
        i += 1
        print(f"I : {i}, Bridge : {bridge}, Wait : {wait}, Bridge_sum : {bridge_sum}")
    return answer

print(solution(10, 12, [1,1,1,1,2,2,4,4,4]))