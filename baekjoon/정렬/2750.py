num = int(input())
numbers = list(map(int, input().split()))

for i in range(0, num-1) :
    for j in range(0, num-i-1) :
        if numbers[j] > numbers[j+1] :
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(*numbers)