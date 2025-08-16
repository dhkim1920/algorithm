# https://www.acmicpc.net/problem/1057

N, JM, HS = map(int, input().split())


def solution(x, y):
    answer = 0
    while x != y:
        x = (x + 1) // 2
        y = (y + 1) // 2
        answer += 1
    return answer


print(solution(JM, HS))