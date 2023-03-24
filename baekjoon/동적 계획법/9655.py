import sys
input = sys.stdin.readline

n = int(input())
winner = ['CY', 'SK']
print(winner[n%2])