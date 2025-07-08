# https://www.acmicpc.net/problem/2775
'''
이건 누적 합이 파스칼 삼격형처럼 이루어지기 때문에 점화식으로 조합 도출하여 푸는 수학문제다.
- n(n + 1)/2 = C(n + 1, 2) 공식을 알거나 유도해 낼수 있어야 한다.
- f(0, n) 과 그 이외의 값을 통해 점화식을 얻어 낼수 있다.

근데 이게 범위가 1 <= k,n <= 14로 매우 작으므로 어려우면 아래와 같이 배열 14개 만들고 이중 포문으로 풀자.
시간제한도 메모리제한도 넉넉하다.
'''

T = int(input())

MAX_K = 14
MAX_N = 14

dp = [[0] * (MAX_N + 1) for _ in range(MAX_K + 1)]

for n in range(1, MAX_N + 1):
    dp[0][n] = n

for k in range(1, MAX_K + 1):
    for n in range(1, MAX_N + 1):
        dp[k][n] = dp[k][n - 1] + dp[k - 1][n]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])
