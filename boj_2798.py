# https://www.acmicpc.net/problem/2798

n, m = map(int, input().split())
cards = list(map(int, input().split()))[:n]

max_v = 0
tmp = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = cards[i] + cards[j] + cards[k]
            if m == tmp:
                max_v = tmp
                break

            if m > tmp:
                if max_v < tmp:
                    max_v = tmp

print(max_v)
