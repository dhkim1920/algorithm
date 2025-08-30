# https://www.acmicpc.net/problem/2839

N = int(input())


def solution():
    for fkg_count in range(N // 5, -1, -1):
        remain = N - (fkg_count * 5)
        if remain % 3 == 0:
            return fkg_count + (remain // 3)
    return -1


print(solution())