# https://www.acmicpc.net/problem/2579

T = int(input())

steps = [0]

for _ in range(1, T + 1):
    steps.append(int(input()))

dp = [0] * (T + 1)


def solution():
    if T <= 0:
        return 0
    elif T == 1:
        return steps[1]
    elif T == 2:
        return steps[1] + steps[2]
    else:
        dp[1] = steps[1]
        dp[2] = steps[1] + steps[2]

        for i in range(3, T + 1):
            dp[i] = steps[i] + max(dp[i-2], (dp[i-3] + steps[i-1]))

    return dp[T]


print(solution())
