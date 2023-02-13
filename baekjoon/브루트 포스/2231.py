import sys
input = sys.stdin.readline

def generator(n) : 
    for i in range(1, 10**6+1) :
        check = i
        temp = i
        while temp >= 1 : 
            check += temp%10
            temp //= 10
        if check == n :
            return i
    return 0

n = int(input())
print(generator(n))