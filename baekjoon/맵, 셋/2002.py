import sys
input = sys.stdin.readline

def count_pass(after) :
    cnt = 0
    for i in range(len(after)) :
        for j in range(i+1, len(after)) :
            if after[i] > after[j] :
                cnt += 1
                break
    return cnt

num = int(input())
before = {}
after = []

for i in range(num) :
    before[input().rstrip()] = i

for i in range(num) :
    after.append(before[input().rstrip()])

print(count_pass(after))