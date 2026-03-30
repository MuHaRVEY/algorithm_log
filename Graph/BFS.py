# BFS 최단 거리 의사코드 (가중치가 모두 1인 그래프)
""""
입력:
	graph      # 인접 리스트, graph[u] = u와 연결된 정점 목록
	start      # 시작 정점
	n          # 정점 개수 (정점 번호: 0 ~ n-1)

출력:
	dist       # start에서 각 정점까지의 최단 거리
			   # 도달 불가면 INF

알고리즘 BFS_Shortest_Distance(graph, start, n):
	dist <- 길이 n인 배열, 모든 값을 INF로 초기화
	visited <- 길이 n인 배열, 모든 값을 False로 초기화
	queue <- 빈 큐

	visited[start] <- True
	dist[start] <- 0
	queue.push(start)

	while queue가 비어있지 않다:
		current <- queue.pop_left()

		for next in graph[current]:
			if visited[next] == False:
				visited[next] <- True
				dist[next] <- dist[current] + 1
				queue.push(next)

	return dist
"""

from collections import deque

def bfs_shortest_distance(graph, start, n):
    INF = float('inf')
    dist = [INF] * n
    visited = [False] * n

    queue = deque()
    visited[start] = True
    dist[start] = 0
    queue.append(start) # 큐에 시작 정점 추가

    while queue: # 큐가 비어있지 않으면 계속 반복
        current = queue.popleft() # 큐에서 가장 앞에 있는 정점 꺼내기

        for next in graph[current]: # current 정점과 연결된 모든 정점에 대해 반복
            if not visited[next]: # next 정점이 아직 방문되지 않았다면
                visited[next] = True # next 정점 방문 처리
                dist[next] = dist[current] + 1 # next 정점까지의 최단 거리 갱신
                queue.append(next) # next 정점을 큐에 추가하여 나중에 방문할 수 있도록 함

    return dist


# BFS 최단 경로 개수 의사코드 (최단 거리 경로가 몇 개인지 계산)
"""
function CountShortestPaths(G, u, v):
    Initialize dist[x] = infinity, paths[x] = 0 for all x in V
    dist[u] = 0, paths[u] = 1
    Queue Q = {u}

    while Q is not empty:
        curr = Dequeue(Q)
        for each neighbor next of curr:
            if dist[next] == infinity:               // 처음 방문
                dist[next] = dist[curr] + 1
                paths[next] = paths[curr]
                Enqueue(Q, next)
            else if dist[next] == dist[curr] + 1:   // 다른 최단 경로 발견
                paths[next] = paths[next] + paths[curr]

    return paths[v]
"""
 

def count_shortest_paths(graph, u, v, n):
    INF = float('inf')
    dist = [INF] * n
    paths = [0] * n

    queue = deque([u])
    dist[u] = 0
    paths[u] = 1

    while queue:
        curr = queue.popleft()

        for next in graph[curr]:
            if dist[next] == INF:
                dist[next] = dist[curr] + 1
                paths[next] = paths[curr] 
                queue.append(next)
            elif dist[next] == dist[curr] + 1:
                paths[next] += paths[curr]

    return paths[v]

# path 출력 예시 5level 정도로
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [5],
        3: [1],
        4: [1, 6],
        5: [2],
        6: [4]
    }


    """
    구조
    0
    ├─ 1
    │  ├─ 3
    |  |  
    │  └─ 4
    │     └─ 6
    2
    └─ 5
    """
    start = 0
    n = 7

    distances = bfs_shortest_distance(graph, start, n)
    print("Shortest distances from vertex", start)
    for vertex in range(n):
        print(f"Vertex {vertex}: Distance {distances[vertex]}")

    u, v = 0, 6
    count = count_shortest_paths(graph, u, v, n)
    print(f"\nNumber of shortest paths from {u} to {v}: {count}")