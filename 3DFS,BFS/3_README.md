# DFS/BFS

## 개요

탐색: 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

- 탐색 문제를 풀려면 DFS와 BFS에 대해 잘 알아야 함.
- 필요한 자료구조: 큐, 스택
- 필요한 함수: 재귀 함수

<큐와 스택 자료 구조를 짤 때 고려해야할 사항>

1. 삽입(push): 데이터 삽입 함수
2. 삭제(pop): 데이터 삭제 함수
3. 오버플로우: 저장공간이 꽉 찾을 때 push 요청을 어떻게할 것인가
4. 언더플로: 저장공간이 비었을 때 pop 요청을 어떻게 처리할 것인가

### 스택: FILO(선입후출) or 후입선출

- 리스트 사용
- 삽입: append() 함수 사용
- 삭제: pop() 함수 사용
- 최하단부터 출력: print(stack)
- 최상단부터 출력: print(stack[::-1])

### 큐: FIFO(선입선출)

- deque 라이브러리 사용: from collections import deque
- 큐 객체 만드는 방법: queue = deque()
- 삽입: append() 함수 사용
- 삭제: popleft() 함수 사ㅇ용
- 먼저 들어온 순서대로 출력하기: print(queue)
- 순서 뒤집기: queue.reverse()
- deque 객체 list 자료형으로 바꾸기: list(queue) 메서트 사용

### 재귀함수: 자기를 다시 호출하는 함수

- 종료 조건을 반드시 명시해야 한다.

### 그래프

- 요소: 노드(정점), 엣지(간선)
- 인접 행렬: 2차원 배열로 그래프의 연결 관계를 표현하는 방식
  - 단점: 모든 관계를 저장하기 때문에 메모리 낭비
  - 장점: 특정 노드가 연결되어 있는지 정보를 얻는 시간이 빠름
- 인접 리스트: 리스트로 그래프의 연결 관계를 표현하는 방식
  - 단점: 특정 노드가 연결되어 있는지 찾는데 시간이 오래 걸림
  - 장점: 연결 정보만 저장하기 때문에 메모리 낭비가 적다

### DFS: 깊이 우선 탐색

- 그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘
- 동작 과정
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
  2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다. (인접 노드가 여러개라면 번호가 낮은 것 부터 처리한다)
  3. 2번 과정을 더 이상 수행할 수 없을 때 까지 반복한다.
- 동작 원리: 스택
- 구현 방법: 재귀 함수

### BFS: 너비 우선 탐색

- 가까운 노드부터 탐색하는 알고리즘
- 동작 과정
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
  2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
  3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복한다.
- 동작 원리: 큐
- 구현 방법: 큐 자료구조 이용