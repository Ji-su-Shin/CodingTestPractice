# 인접 행렬 
## 인접하지 않은 노드 사이에는 INF로 처리한다.
## 나머지는 간선에 걸려있는 비용을 작성 

INF = 999999999

graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(graph)