import sys
input = sys.stdin.readline

start, end, end_s = input().split()
attend = set()
cnt = 0

while True :
    try :
        time, name = input().split()
        if time <= start :
            attend.add(name)
        elif time >= end and time <= end_s :
            if name in attend :
                cnt += 1
                attend.remove(name)
    except :
        print(cnt)
        break
