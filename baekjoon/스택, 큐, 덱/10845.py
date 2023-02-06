import sys
input = sys.stdin.readline

queue = []
front = 0
rear = 0

def push(x) :
    global rear
    queue.append(x)
    rear += 1

def pop() :
    global front
    front += 1
    return queue[front-1]

def size() :
    return rear - front

def empty() :
    if rear == front : 
        return 1
    else :
        return 0

def front_func() :
    return queue[front]

def back() :
    return queue[rear-1]

num = int(input())

for _ in range(num) :
    command = input().rstrip().split()
    if command[0] == 'push' :
        push(command[1])
    elif command[0] == 'pop' :
        if empty() :
            print(-1)
        else :
            print(pop())
    elif command[0] == 'size' :
        print(size())
    elif command[0] == 'empty' :
        print(empty())
    elif command[0] =='front' :
        if empty() :
            print(-1)
        else :
            print(front_func())
    elif command[0] == 'back' :
        if empty() :
            print(-1)
        else : 
            print(back())
