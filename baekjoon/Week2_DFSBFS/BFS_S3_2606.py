## 2606

from collections import deque
com_num, edge_num = int(input()), int(input())
graph = [[] for _ in range(com_num)]

for i in range(edge_num):
    com1, com2 = map(int, input().split())
    graph[com1-1].append(com2)
    graph[com2-1].append(com1)

def bsf (idx, v):
    q = deque()
    q.append(idx)
    v[idx] = True
    cnt = 0
    while q:
        x = q.popleft()
        for j in graph[x]:
            if not v[j-1]:
                v[j-1] = True
                q.append(j-1)
                cnt += 1
    return cnt

visited = [False]*com_num
print(bsf(0, visited))