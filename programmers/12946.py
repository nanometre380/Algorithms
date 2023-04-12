result = []
def hanoi(start, end, inter, n) : 
    if n == 1 :
        result.append([start, end])
    else :
        hanoi(start, inter, end, n-1)
        result.append([start, end])
        hanoi(inter, end, start, n-1)

def solution(n):
    hanoi(1, 3, 2, n)
    return result