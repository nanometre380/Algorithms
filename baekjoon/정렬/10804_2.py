import sys
input = sys.stdin.readline

arr = [i for i in range(0,21)]

def reverse(left, right) :
    arr[left:right+1] = arr[right:left-1:-1]
    return 

for _ in range(10) :
    a, b = map(int, input().split())
    reverse(a, b)

print(*arr[1:])