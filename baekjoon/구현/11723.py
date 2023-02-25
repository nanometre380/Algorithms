# 집합
import sys
input = sys.stdin.readline

def set_add(s, x) :
    s.add(x)
    return s

def set_remove(s, x) :
    try :
        s.remove(x)
        return s
    except :
        return s

def set_check(s, x) :
    if x in s :
        print("1")
    else :
        print("0")

def set_toggle(s, x) :
    if x in s :
        s.remove(x)
    else :
        s.add(x)
    return s

def set_all() :
    return {i for i in range(1,21)}

def set_empty() :
    return set()

s = set()
m = int(input())

for i in range(m) :
    command = input().split()
    if command[0] == 'add' :
        s = set_add(s, int(command[1]))
    elif command[0] == 'remove' :
        s = set_remove(s, int(command[1]))
    elif command[0] == 'check' :
        set_check(s, int(command[1]))
    elif command[0] == 'toggle' :
        s = set_toggle(s, int(command[1]))
    elif command[0] == 'all' :
        s = set_all()
    elif command[0] == 'empty' :
        s = set_empty()
