# https://www.acmicpc.net/problem/1010
import math

T = int(input())
array_n_m = [map(int, input().split()) for i in range(T)]


def solution(n, m):
    return math.comb(m, n)


results = [solution(n, m) for n, m in array_n_m]

for result in results:
    print(f"{result}")
