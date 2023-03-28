musicinfo_dic = {}

"""
def convert_time(time) :
    h, m = map(int, time.split(":"))
    return h*60+m

def check_melody(m, melody) :
    idx = 0
    arr = []
    for i in range(len(melody)) :
        if m[idx] == melody[i] :
            idx += 1
        elif m[0] == melody[i] :
            idx = 1
            arr.append(melody[i])
        else : 
            idx = 0
        if idx == len(m) :
            if i+1 <= len(melody)-1 and melody[i+1] != "#" :
                return True
            elif i == len(melody)-1 : 
                return True
            else : 
                idx = 0
    return False
    
def count_m(melody) :
    cnt = 0
    for m in melody :
        if m != '#' :
            cnt += 1
    return cnt

def append_melody(melody, rest_time) :
    cnt = 0
    rest_music = ""
    for i in range(len(melody)) :
        if melody[i] == "#" :
            rest_music += melody[i]
        else : 
            cnt += 1
            rest_music += melody[i]
        if cnt == rest_time :
            if melody[i+1] == "#" :
                rest_music += melody[i+1]
            return rest_music
    return ""

def make_dic(musicinfos) :
    global musicinfo_dic
    for info in musicinfos :
        t1, t2, title, melody = info.split(",")
        melody = melody.strip()
        len_melody = count_m(melody)
        time = convert_time(t2)-convert_time(t1)
        music = melody*(time//len_melody)+append_melody(melody, time%len_melody)
        musicinfo_dic[title] = music
    musicinfo_dic = sorted(musicinfo_dic.items(), key = lambda x : -count_m(x[1]))
    return musicinfo_dic

def search_music(m) :
    for music, melody in musicinfo_dic :
        if check_melody(m, melody) :
            return music
    return "(None)"

def solution(m, musicinfos):
    answer = ''
    make_dic(musicinfos)
    print(musicinfo_dic)
    return search_music(m)
"""

musicinfo_dic = {}

def change(arr) :
    news = {"C#" : "c", "D#" : "d", "F#" : "f", "G#" : "g", "A#" : "a"}
    for new in news.items() :
        arr = arr.replace(new[0], new[1])
    return arr

def change_time(arr) :
    h, m = map(int, arr.split(":"))
    return h*60+m

def make_infodic(musicinfos) :
    global musicinfo_dic
    for info in musicinfos : 
        t1, t2, title, melody = info.split(",")
        time = change_time(t2) - change_time(t1)
        melody = change(melody)
        music = melody*(time//len(melody)) + melody[:time%len(melody)]
        musicinfo_dic[title] = music
    musicinfo_dic = sorted(musicinfo_dic.items(), key=lambda x : -len(x[1]))
        
def search(m) :
    m = change(m)
    for title, music in musicinfo_dic : 
        if m in music : 
            return title
    else :
        return "(None)"
    

def solution(m, musicinfos) :
    make_infodic(musicinfos)
    print(musicinfo_dic)
    return search(m)
    
    