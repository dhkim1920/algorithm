# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())

type_of_currency = []
for i in range(0, n):
    type_of_currency.append(int(input()))

answer = 0

for i in range(n - 1, -1, -1):
    m = type_of_currency[i]
    if k >= m:
        answer += int(k/m)
        k %= m

    if k <= 0:
        break

print(answer)

