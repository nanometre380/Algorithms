import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = {}

for _ in range(n) :
    input_word = input().rstrip()
    if len(input_word) >= m and input_word not in words : 
        words[input_word] = 1
    elif len(input_word) >= m and input_word in words : 
        words[input_word] += 1

words_list = sorted(words.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for t in words_list : 
    print(t[0])