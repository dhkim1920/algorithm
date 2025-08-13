# https://www.acmicpc.net/problem/9655
# 이 문제는 순서가 정해져있고 1, 3으로 N이 차감되므로 홀수에는 무조건 이긴다.
# 그러나 DP 연습을 위해 점화식을 이용해서 풀어보자

N = int(input())
dp = [False] * N

def solution(n):

    for i in range(4, N):
        dp[i] = (n >= 1 and not dp[i - 1]) or (n >= 3 and not dp[i - 3])

    return dp[n - 1]

print(solution(N))