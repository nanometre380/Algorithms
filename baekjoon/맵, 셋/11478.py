import sys
input = sys.stdin.readline

arr = input().rstrip()
subsets = set()

for i in range(1, len(arr)+1) :
    for j in range(0, len(arr)-i+1) :
        subsets.add(arr[j : j+i])

print(len(subsets))