def solution(n, words):
    answer = []
    games = {}
    prev = words[0][0]
    for i, w in enumerate(words, start=1) : 
        if prev != w[0] :
            return [(i-1)%n+1, (i-1)//n+1]
        else : 
            prev = w[-1]
        if w not in games : 
            games[w] = i
        else : 
            return [(i-1)%n+1, (i-1)//n+1]
    return [0,0]