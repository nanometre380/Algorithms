import sys

input = sys.stdin.readline

priority = {'(':3, ')': 3, '*': 1, '/': 1, '+': 2, '-': 2} # 연산자 우선순위 만들어주기
# ()의 경우에도 비교해주어야 할 일이 생길 수 있으니 3으로 추가
# 가장 낮은 우선 순위로 해야 함

def postfix(string) :   # 후위표기식 변환 함수
    stack = []
    ans = []

    for ch in string :  # 문자 하나씩 반복
        # ch가 피연산자라면
        if ch not in priority : 
            ans.append(ch)
        # 괄호가 시작하면 스택에 넣고
        elif ch == '(' : 
            stack.append(ch) 
        # 괄호가 끝나면 시작괄호가 나올 때 까지의 연산자를 꺼내야 함
        elif ch == ')' :
            while stack and stack[-1] != '(' :
                ans.append(stack.pop())
            stack.pop()     # 시작괄호 제거
        # '+', '-'. '*', '/' 의 경우
        else :
            # 현재 문자의 우선순위가 연산자 스택에 담긴 우선순위보다 낮거나 같다면,
            # 정답에 추가하고 현재 연산자를 연산자 스택에 추가
            while stack and priority[ch] >= priority[stack[-1]] :
                ans.append(stack.pop())
            stack.append(ch)

    # 스택에 남아있는 연산자 모두 꺼내기
    while stack :
        ans.append(stack.pop())
    return ans


string = input().rstrip()
print("".join(postfix(string)))