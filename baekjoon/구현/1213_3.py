import sys
input = sys.stdin.readline

def count_alphabet(text) :
    count = [0] * 26
    for c in text :
        count[ord(c)-65] += 1
    return count

def make_palindrome(count) :
    palindrome = []
    center = []
    for i in range(len(count)) :
        if count[i] %2 != 0 :
            if center :
                return "I'm Sorry Hansoo"
            center.append(chr(i+65))
        palindrome.extend([chr(i+65)]*(count[i]//2))
    return ("".join(palindrome+center+palindrome[::-1]))

arr = input().rstrip()
count = count_alphabet(arr)
print(make_palindrome(count))