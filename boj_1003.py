# https://www.acmicpc.net/problem/1003

T = int(input())
array_n = [int(input()) for i in range(T)]


def solution(n):
    if n <= 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    dp = [[0, 0] for _ in range(n + 1)]
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
    return dp[n]


results = [solution(n) for n in array_n]

for result in results:
    print(f"{result[0]} {result[1]}")
