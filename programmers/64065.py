def solution(s):
    answer = []
    set_by_length = []
    prev = set()
    s = s[2:-2] # 양 옆 괄호 제거
    s = s.split('},{') # 숫자만 남기기 위해 split
    for i in s : 
        temp = set(map(int, i.split(','))) # 집합별로 숫자들을 set으로 만들기
        set_by_length.append(temp)
    set_by_length.sort(key=lambda x : len(x)) # 길이별로 정렬
    
    prev.add(list(set_by_length[0])[0]) # 첫번째 집합의 하나짜리 요소를 넣어주기
    answer.append(list(set_by_length[0])[0])
    for i in range(1, len(set_by_length)) : # 반복문을 돌려가며 차집합을 통해 아직 들어가지 않은 숫자를 구함
        temp = set_by_length[i]-prev
        prev.add(list(temp)[0])
        answer.append(list(temp)[0])
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))