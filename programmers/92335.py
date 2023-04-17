def convert(n, k) :
    res = ""
    while n != 0 :
        res = str(n%k)+res
        n //= k
    print(res)
    return res

def is_prime(n) :
    if n == 1 :
        return False
    for i in range(2, int(n**(0.5))+1) :
        if n%i == 0 : 
            return False
    return True

def solution(n, k):
    answer = 0
    converted = convert(n, k)
    index_zero = []
    
    splitted = converted.split('0')
    
    for sp in splitted :
        if sp and is_prime(int(sp)) == True : 
            answer += 1
    return answer