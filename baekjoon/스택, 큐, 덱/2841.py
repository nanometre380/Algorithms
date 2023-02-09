import sys
input = sys.stdin.readline

lines = [[0] for _ in range(7)]
cnt = 0
line, fret = map(int, input().split())

for _ in range(line) :
    n, f = map(int, input().split())
    while lines[n][-1] > f :
        cnt += 1
        lines[n].pop()
    if lines[n][-1] != f :
        cnt += 1
        lines[n].append(f)

print(cnt)