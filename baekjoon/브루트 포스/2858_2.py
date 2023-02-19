import sys
input = sys.stdin.readline

# room = lxw
# r+b = room
# r = l*2 + w*2 - 4

def get_room(r, b) :
    for w in range(1, r+b+1) :
        if (r+b)%w != 0 :
            continue
        l = (r+b)//w
        if r == (l+w)*2-4 : 
            return l, w

r, b = map(int, input().split())
print(*get_room(r, b))