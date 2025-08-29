# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
type_of_currency = [int(input()) for _ in range(n)]

answer = 0

for i in range(n-1, -1, -1):
    m = type_of_currency[i]
    if k >= m:
        answer += (k//m)
        k %= m

    if k <= 0:
        break

print(answer)

