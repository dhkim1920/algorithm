# https://www.acmicpc.net/problem/2739

n = int(input())

print("\n".join([f"{n} * {i} = {n * i}" for i in range(1, 10)]))


