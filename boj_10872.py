# https://www.acmicpc.net/problem/10872

n = int(input())

if n <= 1:
    print(1)
else:
    result = 1
    for i in range(1, n + 1):
        result *= i

    print(result)
