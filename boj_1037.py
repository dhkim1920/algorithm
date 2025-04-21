# https://www.acmicpc.net/problem/1037

N = int(input())
array = list(map(int, input().split()))


def solution():
    if len(array) <= 1:
        return array[0] * array[0]

    result = sorted(array)
    return result[0] * result[-1]


print(solution())
