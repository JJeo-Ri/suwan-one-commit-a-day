from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

def bfs(x, y):
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      if graph[nx][ny] == 0:
        continue
      
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  return graph[N-1][M-1]

print(bfs(0, 0))



## ------실패한 풀이-------



n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

x = 0
y = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*m for _ in range(n)]
results = []
def dfs(graph, x, y, visited):
	visited[x][y] = True
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
			graph[nx][ny] += graph[x][y]
			if nx == n-1 and ny == m-1:
				results.append(graph[nx][ny])
			dfs(graph, nx, ny, visited)

dfs(graph, x, y, visited)
print(results)