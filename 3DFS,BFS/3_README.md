# DFS/BFS

탐색: 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

- 탐색 문제를 풀려면 DFS와 BFS에 대해 잘 알아야 함.
- 필요한 자료구조: 큐, 스택
- 필요한 함수: 재귀 함수

<큐와 스택 자료 구조를 짤 때 고려해야할 사항>

1. 삽입(push): 데이터 삽입 함수
2. 삭제(pop): 데이터 삭제 함수
3. 오버플로우: 저장공간이 꽉 찾을 때 push 요청을 어떻게할 것인가
4. 언더플로: 저장공간이 비었을 때 pop 요청을 어떻게 처리할 것인가

스택: FILO(선입후출) or 후입선출

- 리스트 사용
- 삽입: append() 함수 사용
- 삭제: pop() 함수 사용
- 최하단부터 출력: print(stack)
- 최상단부터 출력: print(stack[::-1])

큐: FIFO(선입선출)

- deque 라이브러리 사용: from collections import deque
- 큐 객체 만드는 방법: queue = deque()
- 삽입: append() 함수 사용
- 삭제: popleft() 함수 사ㅇ용
- 먼저 들어온 순서대로 출력하기: print(queue)
- 순서 뒤집기: queue.reverse()
- deque 객체 list 자료형으로 바꾸기: list(queue) 메서트 사용

재귀함수: 자기를 다시 호출하는 함수

- 종료 조건을 반드시 명시해야 한다.

```python
def recursive_func():
    print('재귀함수를 호출합니다')
    recursive_func()

recursive_func()
```
