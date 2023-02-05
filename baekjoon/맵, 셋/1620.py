import sys
input = sys.stdin.readline

poke_num, que_num = map(int, input().split())
poke_dic1 = {}
poke_dic2 = {}

for i in range(poke_num) :
    name = input().rstrip()
    poke_dic1[name] = i+1
    poke_dic2[i+1] = name

for _ in range(que_num) :
    query = input().rstrip()
    if query.isdigit() :
        print(poke_dic2[int(query)])
    else :
        print(poke_dic1[query])