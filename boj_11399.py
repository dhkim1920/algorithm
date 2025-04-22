# https://www.acmicpc.net/problem/11399

N = int(input())
array = list(map(int, input().split()))

array.sort()

total = 0
cumulative = 0

for time in array:
    cumulative += time
    total += cumulative

print(total)