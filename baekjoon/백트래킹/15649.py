#N과 M
# n까지의 자연수 중 중복없이 m개를 고른 수열을 모두 구하기
# 중복되는 수열을 여러번 출력하면 안되고, 각 수열은 공백 구분
# 각 수를 넣을 때 이미 수열 내에 있으면 pass
# 해당 수가 현재 수열에서 사용이 되었는지 check하는 배열을 만들기

import sys
input = sys.stdin.readline

arr = []
check = [False for _ in range(9)]

def get_array(n, m) :
    if len(arr) == m : 
        print(*arr)
        return
    
    for i in range(1, n+1):
        #print("!!", i)
        if check[i] == True :
            continue
        arr.append(i)
        check[i] = True
        get_array(n, m)
        #print("ARR : ", arr)
        check[arr.pop()] = False

n, m = map(int, input().split())
#print(len(check))
get_array(n, m)