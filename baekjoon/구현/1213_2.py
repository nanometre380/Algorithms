import sys
input = sys.stdin.readline

def palindrome(arr) :
    alphabets = {}
    half = []
    center = []
    result = []
    for c in arr :
        if c in alphabets : 
            alphabets[c] += 1
        else :
            alphabets[c] = 1
    alphabets = sorted(alphabets.items())

    for c, cnt in alphabets :
        if cnt%2 == 0 :
            half.extend([c]*(cnt//2))
        elif cnt%2 != 0 and center :
            print("I'm Sorry Hansoo")
            return
        elif cnt==1 : 
            center.append(c)
        elif cnt%2 != 0 and cnt > 1 :
            center.append(c)
            half.extend([c]*(cnt//2))
    result = half + center + half[::-1]
    print(''.join(result))

arr = input().rstrip()
palindrome(arr)