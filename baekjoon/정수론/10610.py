# N을 입력받고 그 숫자들을 섞어 30의 배수가 되는 수를 만들자
# 3의 배수 -> 각 자릿수의 합이 3의 배수여야 함
# 10의 배수 -> 마지막 자리가 0이어야 함
# 가장 큰 수 -> sort
import sys

number = input().rstrip()
number = list(map(int, sorted(number)))

if number[0] != 0 or sum(number) % 3 != 0 :
    print("-1")
else : 
    print("".join(map(str, number[::-1])))