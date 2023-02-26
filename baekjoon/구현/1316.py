# 그룹 단어 체커
# 그룹단어 : 각 문자가 연속해서 나타나는 경우 (한 글자가 무리에서 떨어지면 안됨)

import sys
input = sys.stdin.readline

def is_group(word) :
    # 오른쪽에 같은 문자 없음 - 길이 확인
    count = {}
    for i in range(len(word)) :
        if i > 0 and word[i] in count and word[i-1] != word[i] :
            return 0
        if word[i] in count :
            count[word[i]] += 1
        else :
            count[word[i]] = 1
    return 1

n = int(input())
ans = 0
for _ in range(n) :
    word = input().rstrip()
    ans += is_group(word)
print(ans)