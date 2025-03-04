# https://www.acmicpc.net/problem/1541

expression = input()

targets = [sum(map(int, m.split("+"))) for m in expression.split("-")]

answer = targets[0] - sum(targets[1:])

print(answer)