# 요요 시뮬레이션
# 체중 W_0, 일일 에너지 섭취량 = 일일 기초 대사량 l_0, 일일 활동 대사량 A_0
# 다이어트 기간의 일일 에너지 섭취량 = l , 일일 활동 대사량 A
# 체중 변화 = l-(l_0 + A)
# 체중 변화 절댓값이 T 초과라면 일일 기초대사량은 체중변화/2만큼 더해짐
# 일일 기초 대사량 변화는 같은 날의 체중 변화 다음에 일어남
# 체중이 0 이하거나 일일 기초 대사량이 0 이하면 데시는 사망함

# 첫번째 줄에는 일일 기초 대사량의 변화를 고려하지 않았을 때 다이어트 후 예상 체중과 일일 기초 대사량
# 다이어트 전 일일 기초 대사량 그대로 출력 - 데시의 사망이 예상되는 경우 Danger Diet 출력
# 두번째 줄에는 일일 기초 대사량의 변화를 고려했을 때 예상 체중과 일일 기초 대사량

import sys
input = sys.stdin.readline

def calc_weight1(w0, l0, t, d, l, a) :
    before = l0
    w = w0
    e_consume = l0+a
    for i in range(d) :
        e_consume = l0+a
        w += l-e_consume
        if abs(l-e_consume) > t :
            l0 += (l-e_consume)//2
        if l0 <= 0 or w <= 0 :
            print("Danger Diet")
            return
    print(f'{w} {l0}', end = " ")
    if (before-l0) > 0 :
        print("YOYO")
    else :
        print("NO")

def calc_weight2(w0, l0, d, l, a) :
    w = w0
    e_consume = l0 + a
    for i in range(d) :
        w += l-e_consume
        if l0 <= 0 or w <= 0 :
            print("Danger Diet")
            return
    print(f'{w} {l0}')
        

w0, l0, t = map(int, input().split())
d, l, a = map(int, input().split())

calc_weight2(w0, l0, d, l, a)
calc_weight1(w0, l0, t, d, l, a)


