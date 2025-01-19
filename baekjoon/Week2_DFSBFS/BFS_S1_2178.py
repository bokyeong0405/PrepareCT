## 2178

from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def bsf (x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]

print(bsf(0, 0))