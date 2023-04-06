from collections import deque

def diff(cur_word, word) :
    cnt = 0
    for i in range(len(word)) :
        if cur_word[i] != word[i] :
            cnt += 1
    return cnt

def bfs(begin, target, n, words) : #n : len(words)
    checked = [False for _ in range(n)]
    count = {}
    queue = deque()
    queue.append(begin)
    cur_word = ""
    count[begin] = 0
    for w in words :
        count[w] = 0
        
    while queue :
        cur_word = queue.popleft()
        for i, word in enumerate(words) : 
            if diff(cur_word, word) == 1 and checked[i] != True : 
                queue.append(word)
                checked[i] = True
                count[word] = count[cur_word] + 1
        if cur_word == target :
            return count[cur_word]
    if cur_word != target : 
        return 0
                

def solution(begin, target, words):
    answer = 0
    n = len(words)
    answer = bfs(begin, target, n, words)
    return answer