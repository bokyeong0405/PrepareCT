## 1260

from collections import deque
node, edge, vertex = map(int, input().split())
graph = []

# graph 생성
for n in range(node+1):
    graph.append([])
for i in range(edge):
    no, conn_no = map(int, input().split())
    graph[no].append(conn_no)
    graph[conn_no].append(no)
for i in range(len(graph)):
    graph[i].sort()

def bfs (i, v):  # i = 1
    que = deque()
    v[i] = True
    que.append(i)  # 1 추가
    answer = []
    while que:
        x = que.popleft()
        answer.append(x)
        for j in graph[x]:
            if not v[j]:
                que.append(j)
                v[j] = True
    print(" ".join(map(str, answer)))
    return

def dfs (answer, i, v):  # index 1
    v[i] = True
    answer.append(i)
    for j in graph[i]:
        if not v[j]:
            dfs(answer, j, v)
    return answer


ans = []
visited = [False]*(node+1)
print(" ".join(map(str, dfs(ans, vertex, visited))))

visited = [False]*(node+1)
bfs(vertex, visited)
