# https://www.acmicpc.net/problem/1463

N = int(input())

dp = [0] * (N + 1)

def solution ():
    if N == 1:
        return 0
    if N == 2 or N == 3:
        return 1

    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4, N + 1):
        values = [dp[i-1] + 1]

        if i % 2 == 0:
            values.append(dp[i // 2] + 1)
        if i % 3 == 0:
            values.append(dp[i // 3] + 1)

        dp[i] = min(values)

    return dp[N]

print(solution())