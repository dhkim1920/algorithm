# https://www.acmicpc.net/problem/9095

T = int(input())
array_n = [int(input()) for i in range(T)]


def solution(n):
    if n <= 2:
        return n
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n - 1]


results = [solution(n) for n in array_n]

for result in results:
    print(result)
