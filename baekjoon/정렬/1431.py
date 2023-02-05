import sys
input = sys.stdin.readline

n = int(input())
serials = [input().rstrip() for _ in range(n)]

def sum_numbers(arr) :
    sum = 0
    for c in arr : 
        if c.isdigit() :
            sum += int(c)
    return sum

serials.sort(key = lambda x : (len(x), sum_numbers(x), x))

for serial in serials :
    print(serial)
