import sys
input = sys.stdin.readline

test_n = int(input())

def isRemember(first_num, second_num) :
    result = []
    for f in second_num :
        if f in first_num :
            result.append("1")
        else : 
            result.append("0")
    return result

for _ in range(test_n) :
    first_n = int(input())
    first_num = set(map(int, input().split()))
    second_n = int(input())
    second_num = list(map(int, input().split()))
    result = isRemember(first_num, second_num)
    print('\n'.join(result))