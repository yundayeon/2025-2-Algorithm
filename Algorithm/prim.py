
import heapq

# 노드 개수와 간선 개수 입력
v, e = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(v + 1)]

# 모든 간선 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))  # 무방향 그래프

# 프림 알고리즘
def prim(start):
    visited = [False] * (v + 1)
    pq = []
    heapq.heappush(pq, (0, start))  # (비용, 노드)
    total_cost = 0

    while pq:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        total_cost += cost

        for next_cost, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_cost, next_node))

    return total_cost

# 시작 노드는 1번으로 설정
print(prim(1))
