import sys
from math import floor
from collections import Counter
input = sys.stdin.readline

def arithemetic(arr) :
    return floor(sum(arr)/len(arr) + 0.5)

def median(arr) :
    return arr[len(arr)//2]

def mode(arr) :
    cnt = Counter(arr)
    cnt = cnt.most_common()
    if len(cnt) > 1 and cnt[0][1] == cnt[1][1] :
        return cnt[1][0]
    else :
        return cnt[0][0]

def scope(arr) :
    return max(arr) - min(arr)


n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

print(arithemetic(arr))
print(median(arr))
print(mode(arr))
print(scope(arr))