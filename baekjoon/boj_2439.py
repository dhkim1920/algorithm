# https://www.acmicpc.net/problem/2439

n = int(input())

print("\n".join([f"{' ' * (n - i)}{'*' * i}" for i in range(1, n + 1)]))
