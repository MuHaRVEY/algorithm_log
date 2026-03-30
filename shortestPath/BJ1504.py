"""
백준 1504: 특정한 최단 경로

v1과 v2를 반드시 거치고, 서로 같지 않다고 한다.
간선이 최대 1개 존재한다고 한다. (즉, 다중 간선이 없다.) 

핵심 아이디어
- 반드시 거쳐야 하는 정점이 v1, v2일 때 가능한 경로 순서는 2개뿐이다.
  1) 1 -> v1 -> v2 -> N
  2) 1 -> v2 -> v1 -> N
- 각 구간 최단거리는 다익스트라로 구한다.
"""

import heapq
import sys


INF = 10**18


def dijkstra(start, graph, n): #n은 정점의 개수,, 시작 정점을 1번으로 놓았으므로 사용 번호는 1~ n+1로
    distance = [INF] * (n+1) #모두 무한대로 초기화한 거리의 배열이 n+1번까지
    distance[start] = 0 # 시작점의 자신 까지의 거리는 0 
    
    pq = []
    heapq.heappush(pq,(0,start))

    while len(pq) > 0:
        popped = heapq.heappop(pq)
        current_distance = popped[0]
        current_node = popped[1]

        if current_distance > distance[current_node]: # 이미 더 짧은 경로가 발견된 경우 무시
            continue
        
        neighbors = graph[current_node]

        for neighbor in neighbors:
            next_node = neighbor[0]
            edge_cost = neighbor[1]

            next_distance = current_distance + edge_cost

            if next_distance < distance[next_node]: #더 짧아졌다면
                distance[next_node] = next_distance #갱신
                heapq.heappush(pq, (next_distance, next_node)) #우선순위 큐에 저장
    
    return distance




def solve(): 
    input = sys.stdin.readline
    n, e = map(int, input().split())  #입력1. 정점 및 간선 개수
    graph = [[] for _ in range(n + 1)] #인접리스트 graph[i]에는 i번과 연결된 정점들

    for _ in range(e): #입력2. 세개의 정수 a,b,c // a에서 b까지는 양방햘 길이 존재하며 그 길이가 c이다.
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, input().split()) #입력3. 반드시 거쳐야 하는 2개의 서로 다른 정점 v1, v2

    dist_from_1 = dijkstra(1, graph, n)
    dist_from_v1 = dijkstra(v1, graph, n)
    dist_from_v2 = dijkstra(v2, graph, n)

    route1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
    route2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

    answer = min(route1, route2)
    print(-1 if answer >= INF else answer)


if __name__ == "__main__":
    solve()
