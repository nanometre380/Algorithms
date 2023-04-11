from collections import deque
def compression(n, s) :
    new_str = ""
    for j in range(len(s)) :
        if j%n == 0 and j!=0: 
            new_str += ","
        new_str += s[j]
    new_str = new_str.split(",")
    queue = deque(new_str)
    save = []
    result = ""
    while queue : 
        if not save :
            save.append(queue.popleft())
        elif save[-1] == queue[0] :
            save.append(queue.popleft())
        elif save[-1] != queue[0] :
            if len(save) == 1 :
                result += save[0]
            else : 
                result += (str(len(save))+save[0])
            save = []
    if len(save) == 1 :
        result += save[0]
    else : 
        result += (str(len(save))+save[0])
    return result

def solution(s):
    answer = s
    for i in range(1, len(s)+1) :
        temp = compression(i, s)
        #print(temp)
        if len(answer) > len(temp) :
            answer = temp
        #print("answer : ", answer)
    return len(answer)