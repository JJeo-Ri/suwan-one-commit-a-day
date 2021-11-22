from pprint import pprint

n = int(input())

graph = [list(input()) for _ in range(n)]


# 스택을 이용한
visited = [[False] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, graph, visited):
    global cnt
    cnt += 1
    x = int(x)
    y = int(y)
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                if graph[nx][ny] == "1":
                    graph[nx][ny] = int(graph[x][y]) + 1
                    dfs(nx, ny, graph, visited)


answer = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == "1":
            cnt = 0
            dfs(x, y, graph, visited)
            answer.append(cnt)
print(len(answer))
answer.sort()
[print(ans) for ans in answer]
