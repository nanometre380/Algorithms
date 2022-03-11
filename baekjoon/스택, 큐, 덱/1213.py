import sys

input = sys.stdin.readline

def count_alphabet(text) :
    cnt = [0] * 26
    for c in text[:-1] :
        cnt[ord(c) - 65] += 1
    return cnt

def make_palindrome(cnt) :
    palindrome = []
    center = []

    for i in range(26) :
        if cnt[i]%2 == 1 :
            if len(center) != 0 :
                return "I'm Sorry Hansoo"
            center.append(chr(i+65))
        
        palindrome.extend([chr(i+65)]*(cnt[i]//2))

    return "".join(palindrome+center+palindrome[::-1])
        
name = input()
cnt = count_alphabet(name)
print(make_palindrome(cnt))

