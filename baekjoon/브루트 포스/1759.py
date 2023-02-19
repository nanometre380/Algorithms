# 암호 만들기
# L개의 알파벳 소문자 : aeiou 최소 하나, 자음  최소 두개, 알팝벳 오름차순
# C 개의 문자가 주어졌을 때 가능성이 있는 암호 구하기

import sys
from itertools import combinations

input = sys.stdin.readline

l, c = map(int, input().split())
alphabet = input().split()
alphabet.sort()
candid = combinations(alphabet, l)
vowels = ['a', 'e', 'i', 'o', 'u']
for i in candid :
    cnt_vowel = 0
    cnt_conso = 0
    for j in i :
        if j in vowels : 
            cnt_vowel += 1
        else : 
            cnt_conso += 1
    if cnt_vowel == 0 :
        continue
    elif cnt_conso < 2 :
        continue
    print("".join(i))
    