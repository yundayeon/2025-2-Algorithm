
# Bellman-Ford Algorithm in Python

def bellman_ford(n, edges, start):
    # 거리 배열 초기화
    INF = float('inf')
    distance = [INF] * n
    distance[start] = 0

    # (n-1)번 반복
    for _ in range(n - 1):
        for u, v, w in edges:
            if distance[u] != INF and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # 음수 사이클 확인
    for u, v, w in edges:
        if distance[u] != INF and distance[u] + w < distance[v]:
            print("음수 사이클 존재!")
            return None

    return distance


# 예시 실행
if __name__ == "__main__":
    # 정점 개수와 간선 리스트
    n = 5
    edges = [
        (0, 1, 6),
        (0, 2, 7),
        (1, 2, 8),
        (1, 3, 5),
        (1, 4, -4),
        (2, 3, -3),
        (2, 4, 9),
        (3, 1, -2),
        (4, 0, 2),
        (4, 3, 7)
    ]

    start = 0
    result = bellman_ford(n, edges, start)
    print("최단 거리:", result)
