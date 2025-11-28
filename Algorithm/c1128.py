import sys
import heapq
##힙 정렬의 대해 기말고사 문제가 나올 수도 있음

try:
    sys.stdin = open('9_input.txt', 'r', encoding = 'utf-8')
    sys.stdout = open('9_output.txt', 'w', encoding = 'utf-8')
except Exception as e:
    pass

#무한대 값 설정 (최단 거리 초기화용)
INF = int(1e9)

def main():
    dijkstra1()
    dijkstra2()
    floyd()
    example1()
    example2()
    
def read_dijkstra_input():
    n,m = map(int,input().split())
    start = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
    return n, start, graph

def get_smallest_node(m, distance, visited):
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
    
def dijkstra1():
    print("기본 다익스트라")
    n, m, start, graph = read_dijkstra_input()
    visited = [False] * (n + 1)
    distance = [INF] * (n+1)
    
    distance[start] = 0
    visited[start] = True
    for node, cost in graph[start]:
        distance[node] = cost
    
    for _ in range(n-1):
        now = get_smallest_node(n, distance, visited)
        visited[now] = True
        for node, cost in graph[now]:
            if distance[now] + cost < distance[node]:
                distance[node] = distance[now] + cost
                
    for i in range(1, n +1):
        print("INFINITY" if distance[i] == INF else distance[i])
        
def dijkstra2():
    print("힙 기반 다익스트라")
    n, m, start, graph = read_dijkstra_input()
    distance = [INF] * (n + 1)
    
    #힙 생성을 위한 리스트 하나 만들고 초기화
    q = []
    
    #시작 노드 넣기
    #힙에 넣을 때 거리가 운선순위가 되므로, 거리값을 튜플의 앞에 둔다.
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(q, (new_cost, node))
        print(q)
        
        for i in range(1, n + 1):
            print("INFINITY" if distance[i] == INF else distance[i])    
            
            
def read_floyd_input():
    print("플로이드 - 워셜 데이터 읽기")
    n, m = map(int, input().split())
    matrix = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        matrix[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        matrix[a][b] = c
    return n, m, matrix

def floyd():
    print("플로이드 워셜") 
    
    n, m, matrix = read_floyd_input()
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                
    for row in matrix[1:]:
        print(" ".join("INF" if x == INF else str(x) for x in row[1:]))
    
    
def read_exaple1_input():
    print("예제1 데이터 읽기")
    n, m = map(int, input().split())
    
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0
        
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1
        
    x, k = map(int, input().split())
    return n, graph, x, k

def example1():
    print("예제 1 (x,k 거쳐가는 최단 거리)")
    
    n, graph, x, k = read_exaple1_input()
    
    for mid in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][mid] + graph[mid][b])
                
    distance = graph[1][k] + graph[k][x]
    print(distance if distance < INF else -1)
    
def read_example2_input():
    print("예제2 데이터 읽기")
    n, m, start = map(int,input().split())
    graph =[[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, z = map(int, input().split())
        graph[x].append((y,z))
    return n, m, start, graph
    
    
def example2():
    print("예저2 (도달 가능한 노드 개수 + 최대 거리)")
    
    n, m, start, graph = read_example2_input()
    distance = [INF] * (n + 1)
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while 1:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, cost in graph[now]:
            new_cost = dist + cost
        if new_cost < distance[node]:
            distance[node] = new_cost
            heapq.heappush(q, (new_cost, node))
            
    count = sum(1 for d in distance if d != INF)
    max_distance = max(d for d in distance if d != INF)
    print(count -1, max_distance)
    
    
    
if __name__ == "__main__":
    main()