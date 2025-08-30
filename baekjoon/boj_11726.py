# https://www.acmicpc.net/problem/11726

input_n = int(input())

def solution(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    return dp[n]

print(solution(input_n))
