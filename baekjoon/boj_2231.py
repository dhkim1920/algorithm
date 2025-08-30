# https://www.acmicpc.net/problem/2231

n_input = int(input())


def solution(n):
    if n == (0 or 1):
        return 0

    for i in range(1, n + 1):
        if i <= 9:
            tmp = i + i
        else:
            tmp = i + sum(map(int, str(i)))

        if tmp == n:
            return i

    return 0


print(solution(n_input))
