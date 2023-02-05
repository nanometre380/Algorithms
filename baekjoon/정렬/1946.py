import sys
input = sys.stdin.readline

"""
"서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다."
즉, 서류 심사 점수가 낮아도 면접 점수가 다른 서류 심사 점수가 높은 사람보다 높다면 선발한다는 의미
서류 심사 성적 순으로 정렬한 뒤 면접 성적이 앞선 서류 심사 성적이 좋은 사람보다 좋다면 선발한다. 
"""

n = int(input())

for _ in range(n) :
    people = int(input())
    ranks = [list(map(int, input().split())) for _ in range(people)]
    answer = 1

    ranks.sort()

    best_int = ranks[0][1]

    for rank in ranks :
        if best_int > rank[1] :
            best_int = rank[1]
            answer += 1

    print(answer)
