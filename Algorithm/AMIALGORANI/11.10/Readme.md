### 1520 내리막길
#### [문제 정의]
1. (0,0)에서 (m-1,n-1)까지 가는데 높이가 이미 정해져 있고, 높이는 높은 곳에서 낮은 곳으로만 갈 수 있다.
2.  BFS를 이용하여 각 지점에서 자신보다 낮은 곳을 큐에 추가하여, 큐가 없을때까지 반복한다.

#### [시행 착오..?]
+ BFS를 통해 queue로 모든 부분을 반복하면 2초의 시간제한에 걸린다.
+ DP와 BFS를 같이 사용해서 방문한 곳은 다시 방문하지 않게 한다.
+ DP를 사용하려면, 원래 사용하던 deque말고, heapq를 사용하여서 우선 순위가 높은, 즉 숫자가 높은 곳을 먼저 간다음 낮은 숫자를 방문하여 업데이트 해주어야 한다.  
+ Python에서 heapq는 최소 힙이다

#### [사용한 알고리즘]
+ BFS, DP
+ heapq ( priority queue )


### 1325 효율적인 해킹
#### [문제 정의]
1. 자식 노드가 젤 많은 노드 찾기

#### [시행 착오..?]
+ 메모리 초과 때문에 graph를 list에서 dictionary로 바꿈
+ 15번째 줄 추가하지 않으면 출력 초과
+ 시간 초과 -> pypy3 사용
+ 방문 노드 다시 방문 X

#### [사용한 알고리즘]
+ BFS
+ defaultdict() -> from collections 


### 1068 트리
#### [문제 정의]
1. 트리에서 노드 제거했을때 리프 노드의 개수

#### [시행 착오..?]
+ 조건 주기 개빡센듯 


#### [사용한 알고리즘]
+ BFS
+ defaultdict() -> from collections 