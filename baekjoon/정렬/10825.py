import sys

n = int(sys.stdin.readline())

main_list = [0 for _ in range(n)]

for i in range(n) :
    [name, kor, eng, math] = sys.stdin.readline().split()
    main_list[i] = [name, int(kor), int(eng), int(math)]

sorted_list = sorted(main_list, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for score in sorted_list :
    print(score[0])
