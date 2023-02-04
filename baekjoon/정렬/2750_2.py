num = int(input())
numbers = list(map(int, input().split()))

for i in range(0, num-1) :
    isSwap = False
    for j in range(0, num-i-1) :
        if numbers[j] > numbers[j+1] : 
            isSwap = True
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    if not isSwap :
        break
print(*numbers)