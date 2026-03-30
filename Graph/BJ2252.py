#2252 줄세우기
# DAG
# DFS 방식은 재귀로 인해 다소 비효율적으로 보임
"""
참고한 내용들이다.
Algorithms - Sanjoy Dasgupta, Christos H. Papadimitriou, ... 참고 중.

진입 차수(In-degree) 계산: 그래프의 모든 정점에 대해 자신에게 들어오는 간선의 개수(진입 차수)를 계산하여 배열에 저장합니다.
큐(Queue) 초기화: 진입 차수가 0인 모든 정점(즉, 먼저 수행해야 할 선행 조건이 없는 소스 노드들)을 찾아 큐에 삽입합니다.
BFS 탐색 (간선 삭제 및 새 소스 탐색): 큐가 빌 때까지 다음 과정을 반복합니다.

큐에서 가장 앞의 정점 u를 꺼내어 위상 정렬 결과 리스트에 추가합니다.
정점 u에서 뻗어나가는 모든 간선 (u,v)를 확인하며, 도착 정점 v의 진입 차수를 1씩 감소시킵니다. 
(이는 교재에서 설명한 '해당 노드와 간선을 그래프에서 완전히 지워버리는 작업'을 수학적으로 구현한 것)

진입 차수를 감소시킨 결과 새롭게 진입 차수가 0이 된 정점(새로운 소스 노드)이 생겼다면, 그 정점을 큐에 새롭게 삽입합니다.

종료 및 사이클 판별: 큐가 비어서 탐색이 종료되었을 때, 결과 리스트에 모든 정점이 순서대로 포함되어 있다면 위상 정렬이 완성된 것입니다. 
만약 결과 리스트에 빠진 정점이 있다면 그래프에 사이클이 존재하여 위상 정렬이 불가능한 상태임을 의미합니다.
"""
import sys
from collections import deque

def solve():
    # n명, m은 키를 비교한 횟수
    # m개의 줄에는 키를 비교한 두 학생 a,b의 번호  -> 이때, a는 b보다 앞선다는 의미.
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)] #1부터 N 까지 인접리스트 생성
    indegree = [0] * (n + 1)

    # 위상 정렬에서의 조건은 선행 조건이 없는 노드부터 처리하는 것
    # indegree == 0을 찾아야 선행 조건이 없는 것을 수치로 확인 가능

    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    q = deque() # 큐 생성
    for i in range(1, n + 1):
        if indegree[i] == 0: #진입차수 0인 정점들
            q.append(i) #해당 정점들 모두 큐에 추가
    
    order = []
    while q:
        current = q.popleft()
        order.append(current) #큐에서 가장 앞으로 정점을 꺼내어 리스트에 추가

        for next in graph[current]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    print(*order)  #파이썬도 개별 인자로 출력할 수 있다는 걸 처음 알음 ㄷㄷ 

if __name__ == "__main__":
    solve()
