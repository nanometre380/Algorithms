import sys

n = int(sys.stdin.readline())

points_list = [0 for _ in range(n)]

for i in range(n) :
    [x, y] = map(int, sys.stdin.readline().split())
    points_list[i] = [x, y]

sorted_list = sorted(points_list, key = lambda x : (x[1], x[0]))

for points in sorted_list :
    print(str(points[0]) +" "+str(points[1]))
