# https://www.acmicpc.net/problem/1026

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

result = 0
for i in range(N):
    m = max(B)
    result += (A[i] * m)
    B.remove(m)

print(result)
