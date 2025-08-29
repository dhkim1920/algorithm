# https://www.acmicpc.net/problem/1292

A, B = map(int, input().split())

arr = [1]

number = 2
count = 1

for i in range(B + 1):
    arr.append(number)
    if number == count:
        number += 1
        count = 1
        continue

    count += 1

print(sum(arr[A-1:B]))