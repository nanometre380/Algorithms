import sys
input = sys.stdin.readline

def combi() :
    if m == 1 :
        return n
    mc[0] = 0
    mc[1] = n 
    for i in range(2, m+1) :
        mc[i] = mc[i-1]*((n-(i-1)))//i
    return mc[m]

n, m = map(int, input().split())
mc = [0 for _ in range(m+1)]
combi()
print(combi())