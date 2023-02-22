# 감독관 : 총감독관, 부감독관
# 총감독관 : 한 시험장에서 B명 감시 / 부감독관은 C명 감시
# 총감독관 한 명 부감독관 여러명
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0

ans += n
a = list(map(lambda x : x-b, a))

for r in a :
    if r <= 0 :
        continue
    ans += r//c
    if r%c != 0 :
        ans += 1

print(ans)
