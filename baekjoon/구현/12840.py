import sys
input = sys.stdin.readline

MIN = 60
HOUR = MIN*60
DAY = HOUR*24

h, m ,s = map(int, input().split())
time = h*HOUR + m*MIN + s


def time_print(time) :
    h = time//HOUR
    time %= HOUR
    m = time//MIN
    time %= MIN
    print(h, m, time)

def time_coordi(seconds) :
    global time
    time += seconds
    time = time%DAY
    
num = int(input())
for _ in range(num) :
    query = list(map(int, input().split()))
    if query[0]==1: 
        time_coordi(query[1])
    elif query[0] == 2 :
         time_coordi(-query[1])
    elif query[0]==3:
        time_print(time)
