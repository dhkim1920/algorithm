
ice_tray = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

N = len(ice_tray)
M = len(ice_tray[0])


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= N or y >= M:
        return False

    if ice_tray[x][y] == 0:
        ice_tray[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    else:
        return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)
