def solution(s):
    s = s.split()
    numbers = [f'{i}' for i in range(10)]
    answer = []
    for i in s :
        left = i[0]
        right = i[1:]
        right = right.lower()
        print(right)
        if left not in numbers :
            left = left.upper()
        print(left)
        answer.append(left+right)
    return " ".join(answer)

s = "two  space"
print(solution(s))
