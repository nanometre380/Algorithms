# 다시 풀기
import sys
input = sys.stdin.readline

add = lambda x, y : x+y
sub = lambda x, y : x-y
multi = lambda x, y : x*y
def div(x, y) :
    if x > 0 :
        return x//y
    else : 
        return -(-x//y)

calc = [add, sub, multi, div]

def get_minmax(cnt, value) :
    global min_value, max_value
    if cnt == n : 
        min_value = min(value, min_value)
        max_value = max(value, max_value)
        return
    for i in range(4) :
        if ops[i] > 0 : 
            ops[i] -= 1
            get_minmax(cnt+1, calc[i](value, a[cnt]))
            ops[i] += 1
    return
    


n = int(input())
a = list(map(int, input().split()))
ops = list(map(int, input().split()))
min_value = 10e9
max_value = -10e9

get_minmax(1, a[0])
print(max_value, min_value, sep='\n')