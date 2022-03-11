import sys

n = int(sys.stdin.readline())
chicken = list(map(int,input().split()))
k = int(sys.stdin.readline())
sorted_list = []

for i in range(0, n, n//k) :
    sorted_list += sorted(chicken[i:i+n//k])

for i in sorted_list :
    print(i, end=' ')

