import sys

input = sys.stdin.readline

def prime_factor(k) :
    # 숫자에 해당하는 인덱스에 그 수를 나누는 소인수를 담는 배열 만들기
    max_n = max(k)
    arr = [0 for i in range(max_n+1)]

    for i in range(2, max_n+1) :    # 주의! int(max_n+1**(1/2))는 내림이라 사용X
        if arr[i] != 0 :
            continue
        for j in range(i*i, max_n+1, i) :   # i*(i-1)까지는 이미 처리되었으므로 i*i부터 시작
            if arr[j] == 0 :
                arr[j] += i
    
    return arr

def print_factors(k, arr) :
    # 앞서 구한 배열을 통해 소인수들을 모두 출력하는 함수
    for i in k :
        num = i
        factors = []
        while arr[num] != 0:    # 인덱스의 소인수가 없을 때까지
            factors.append(arr[num])
            num = num//arr[num]
        factors.append(num)     # 마지막 소수를 추가
        print(" ".join(map(str, factors)))



n = int(input())
k = list(map(int, input().split()))
arr = prime_factor(k)
print_factors(k, arr)