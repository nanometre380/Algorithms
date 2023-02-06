import sys
input = sys.stdin.readline

stack = []
top = -1

def push(x) :
    global stack
    global top
    top += 1
    stack.insert(top, x)

def pop() :
    global top
    if top < 0 :
        return -1
    top -= 1
    return stack[top+1]

def size() :
    return top+1

def empty() :
    if top == -1 : 
        return 1
    else :
        return 0

def top_func() :
    if top == -1 :
        return -1
    else : 
        return stack[top]

num = int(input())
for _ in range(num) :
    command = input().split()
    if command[0] == 'push' :
        push(command[1])
    elif command[0] == 'pop' :
        print(pop())
    elif command[0] == 'size' :
        print(size())
    elif command[0] == 'empty' :
        print(empty())
    elif command[0] =='top' :
        print(top_func())