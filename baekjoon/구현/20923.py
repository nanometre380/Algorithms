# 숫자 할리갈리 게임
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
deck = [deque(), deque()] #0 : do, 1: su
ground = [deque(), deque()] #0 : do, 1 : su

def merge(hit) :
    deck[hit].extendleft(ground[1-hit])
    deck[hit].extendleft(ground[hit])
    ground[0].clear()
    ground[1].clear()

def playing() :
    for i in range(m) : #0~m-1
        hit = 5
        ground[i%2].append(deck[i%2].pop())
        if not deck[i%2] :
            return (i+1)%2
        if ground[0] and ground[1] and ground[0][-1] + ground[1][-1] == 5 : 
            hit = 1
        elif (ground[0] and ground[0][-1] == 5) or (ground[1] and ground[1][-1] == 5) :
            hit = 0
        if hit != 5 :
            merge(hit)
    if len(deck[0]) > len(deck[1]) :
        return 0
    elif len(deck[0]) < len(deck[1]) :
        return 1
    else :
        return 2
        

for i in range(n) :
    result = ["do", "su", "dosu"]
    do, su = map(int, input().split())
    deck[0].append(do)
    deck[1].append(su)
#print(deck)
print(result[playing()])
