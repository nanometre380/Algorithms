import sys
input = sys.stdin.readline

def mergesort(numbers) :
    """
    병합정렬
    """
    if len(numbers) <= 1 :
        return numbers

    mid = len(numbers)//2
    left = mergesort(numbers[:mid])
    right = mergesort(numbers[mid:])

    l = r = 0
    merged = []

    while l < len(left) and r < len(right) :
        if left[l] < right[r] :
            merged.append(left[l])
            l += 1
        else :
            merged.append(right[r])
            r += 1
    merged += left[l:]
    merged += right[r:]

    return merged

n = int(input())
numbers = []
for _  in range(n) :
    numbers.append(int(input()))


result = mergesort(numbers)

print(*result)

