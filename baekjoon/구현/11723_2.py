import sys

input = sys.stdin.readline

set_list = [False for _ in range(21)]

m = int(input())

for i in range(m) :
    command = input().split()
    if command[0] == 'add' :
        set_list[int(command[1])] = True
    elif command[0] == 'remove' :
        set_list[int(command[1])] = False
    elif command[0] == 'check' :
        print(int(set_list[int(command[1])]))
    elif command[0] == 'toggle' :
        set_list[int(command[1])] = not set_list[int(command[1])]
    elif command[0] == 'all' :
        set_list = [True for _ in range(21)]
    elif command[0] == 'empty' :
        set_list = [False for _ in range(21)]