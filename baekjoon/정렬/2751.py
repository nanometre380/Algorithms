import sys
n = int(sys.stdin.readline())
numbers = [0 for _ in range(n)]

for i in range(n) :
    numbers[i] = int(sys.stdin.readline())

numbers.sort()

for i in numbers :
    print(i)
