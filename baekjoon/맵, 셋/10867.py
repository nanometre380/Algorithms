import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers = list(set(numbers))
numbers.sort()

print(*numbers)