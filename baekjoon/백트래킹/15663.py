import sys
input = sys.stdin.readline

def make_arr() :
    if len(arr) == m :
        print(*arr)
        return 
    prev = 0
    for i in range(len(numbers)) :
        if not check[i] and prev != numbers[i]:
            arr.append(numbers[i])
            check[i] = True
            prev = numbers[i]
            make_arr()
            arr.pop()
            check[i] = False


n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
check = [False for _ in range(len(numbers))]
arr = []
make_arr()
