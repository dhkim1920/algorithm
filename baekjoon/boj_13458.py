# https://www.acmicpc.net/problem/13458

N = int(input())
arr = map(int, input().split())
B, C = map(int, input().split())

result = 0
for a in arr:
    result += 1
    tmp = a - B
    if tmp > 0:
        result += (tmp + C - 1) // C # 올림 공식

print(result)
