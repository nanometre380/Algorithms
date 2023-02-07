import sys
from collections import Counter

input = sys.stdin.readline

def arithemetic(x) :
    return round(sum(x)/len(x))

def median(x) :
    x.sort()
    return x[(len(x)//2)]

def frequent(x) :
    c = Counter(x).most_common()
    c.sort(key=lambda x : (-x[1], x[0]))
    if len(c) > 1 and c[0][1] == c[1][1] :
        return c[1][0]
    return c[0][0]

def cover(x) :
    return max(x) - min(x)


n = int(input().rstrip())
numbers = []

for _ in range(0, n) : 
    numbers.append(int(input()))

print(arithemetic(numbers))
print(median(numbers))
print(frequent(numbers))
print(cover(numbers))

