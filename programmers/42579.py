def solution(genres, plays):
    answer = []
    g_plays = {}
    song_plays = {}
    
    for i in range(len(genres)) :
        k = genres[i]+"-"+str(i)
        song_plays[k] = plays[i]
        if genres[i] not in g_plays.keys() :
            g_plays[genres[i]] = plays[i]
        else :
            g_plays[genres[i]] += plays[i]
    
    g_plays = sorted(g_plays.items(), key=lambda x : -x[1])
    song_plays = sorted(song_plays.items(), key=lambda x : (-x[1], x[0]))
    
    for g in g_plays :
        g_temp = g[0]
        s_max = 0
        for song in song_plays :
            if s_max == 2 :
                break
            song_g, song_no = song[0].split('-')
            if g_temp == song_g : 
                answer.append(int(song_no))
                s_max += 1
        
    return answer