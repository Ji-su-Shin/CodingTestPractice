# BFS

from collections import deque
from tkinter.tix import Tree

def bfs(graph, start, visited):
    # 큐 만들기
    q = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    # 큐가 빌 때 까지 반복
    while q:
        # 큐에서 원소 하나 뽑아서 출력
        v = q.popleft()
        print(v, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

bfs(graph, 1, visited)