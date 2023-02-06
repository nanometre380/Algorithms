import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    products = {}
    cases = 1
    num = int(input())
    for _ in range(num) :
        product = input().rstrip().split()[1]
        if product in products :
            products[product] += 1
        else :
            products[product] = 1
    for kind in products.values() :
        cases *= (kind+1)

    print(cases-1)