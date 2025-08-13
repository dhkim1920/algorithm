# https://www.acmicpc.net/problem/9655
# 이 문제는 순서가 정해져있고 1, 3으로 N이 차감되므로 홀수에는 무조건 이긴다.
# N = int(input())
# print("SK" if N % 2 else "CY")
# 그러나 DP 연습을 위해 점화식을 이용해서 풀어보자

N = int(input())
dp = [False] * (N + 1)


def solution(n):
    dp[1] = True
    if N >= 3:
        dp[3] = True

    for i in range(4, n + 1):
        dp[i] = not dp[i - 1] or not dp[i - 3]

    return "SK" if dp[n] else "CY"


print(solution(N))
