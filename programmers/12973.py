def solution(s):
    # 스택을 사용해서 시간복잡도를 줄이는 데에 집중해야 하는 문제임
    j = 0
    stk = []
    while True :
        if stk and stk[-1] == s[j] :
            stk.pop()
            j += 1
        else : 
            stk.append(s[j])
            j = j+1
        if j == len(s) and not stk : 
            return 1
        elif j == len(s) and stk :
            return 0