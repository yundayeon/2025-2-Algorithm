
''' 10장 총정리 파일 '''
import sys

# 파일 입출력 설정
try:
    sys.stdin = open("ch10_input.txt", "r", encoding="utf-8")
    # sys.stdout = open("ch10_output.txt", "w", encoding="utf-8")
    sys.stdout = open("ch10_output.txt", "a", encoding="utf-8")
except FileNotFoundError:
    print("입출력 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"파일 설정 오류: {e}")

# -------------------------------------------------------------------    
# Main Function
# ------------------------------------------------------------------- 

sw = 2 # flag variable

def main():
    ''' main function'''
    e, parent = matualFn()
    cycleFn(e, parent)
    kruskalFn()
    primFn()
    topological_sortFn()
    # team_formation_problem()
    # split_city()
    # curriculum_design()
    

# -------------------------------------------------------------------    
# 서로 소 집합 알고리즘 소스코드 1
# -------------------------------------------------------------------
#특정 원소가 속한 집합을 찾기

def matualFn():
    v, e, parent = read_input()  # 입력 처리
    print_output(v, parent)  # 결과 출력

    return e, parent  # 사이클에서 사용하기 위해 반환

def read_input():
    v, e = map(int, input().split())
    parent = [i for i  in range(v+1)]
    
    for i in range(e):
        a,b = map(int, input().split())
        union_parent(parent,a,b)
        
    return v, e, parent

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a!=b:
        parent[b]=a
        
# def find_parent(parent, x):
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

def print_output(v, parent):
    #각 원소가 속한 집합 출력하기
    print('각 원소가 속한 집합:', end='')
    for i in range(1, v+1):
        print(find_parent(parent,i), end='')
    
    print()
    
    #부모 테이블 내용 출력하기
    print('부모 테이블', end='')
    for i in range(1, v+1):
        print(parent[i], end='')
        
    print()
    
    
# -------------------------------------------------------------------    
# Ex 2. 서로 소 집합 알고리즘 소스코드
# -------------------------------------------------------------------    
def find_parent(parent, x):
    # 1번 부모 찾기, 자신을 돌려주는 함수
    if sw == 1:
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            return find_parent(parent, parent[x])
        return x
    # 2번 부모 정점을 돌려주는 함수
    elif sw == 2:
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    
# -------------------------------------------------------------------
# Ex 3. 사이클 발생 여부 판단하기
# -------------------------------------------------------------------
def cycleFn(e= None, parent= None):
    ''' 사이클 발생 여부 판단하기 '''

    cycle = False  # 사이클 발생 여부
    
    v, e = map(int, input().split())
    for _ in range(e):
        a, b = map(int, input().split())
        #사이클이 발생한 경우 종료
        if find_parent(parent,a) == find_parent(parent, b):
            cycle = True
            #break
        else:
            union_parent(parent, a, b)
            
    if cycle:
        print("사이클이 발생했습니다")
    else:
        print("사이클이 발생하지 않았습니다")


# -------------------------------------------------------------------
# Ex 4. 크루스칼 알고리즘 소스코드
# -------------------------------------------------------------------
def kruskalFn():
    ''' 크루스칼 알고리즘 소스코드 '''
    v, e = map(int, input().split())
    parent = [0] * (v + 1)  # 부모 테이블 초기화하기

    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i
        
    edges = []
    total_cost = 0
    
    #모든 간선에 대한 정보 입력 받기
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    
    #간선을 비용순으로 정렬
    edges.sort()
    
    #간선을 하나씩 확인하며
    for edge in edges:
        cost, a, b = edge
        #사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent,a) != find_parent(parent, b):
            union_parent(parent,a,b)
            total_cost += cost
            
    print(f"크루스칼 알고리즘을 이용한 최소 신장 트리의 총 비용: {total_cost}")
        


# -------------------------------------------------------------------
# Ex 5. Prim 알고리즘
# -------------------------------------------------------------------
import heapq

def primFn():
    ''' 프림 알고리즘 소스코드 '''
    v, e = map(int, input().split())  # 정점 개수, 간선 개수
    graph = [[] for _ in range(v + 1)]  # 인접 리스트 초기화
    
    #모든 간선 정보 입력
    #무방향 그래프
    for _ in range(e):
        a, b, cost = map(int, input().split())
        graph[a].append((cost,b))
        graph[b].append((cost,a))
        
    visited = [False] * (v + 1)
    min_heap = [] #heap, MinHeap
    total_cost = 0
    
    #1번 노드에서 시작
    visited[1] = True
    for edge in graph[1]:
        heapq.heappush(min_heap, edge)
        
    while min_heap:
        cost,node = heapq.heappop(min_heap)
        if not visited[node]:
            visited[node] = True
            total_cost += cost
            for next_edge in graph[node]:
                if not visited[next_edge[1]]:
                    heapq.heappush(min_heap, next_edge)
                    
    print(f"프림 알고리즘을 이용한 최소 신장 트리의 총 비용: {total_cost}")


# -------------------------------------------------------------------
# Ex 6. 위상 정렬 소스코드
# -------------------------------------------------------------------
from collections import deque

def topological_sortFn():
    v, e = map(int, input().split())  # 노드 개수, 간선 개수
    indegree = [0] * (v + 1)  # 진입 차
    graph = [[] for _ in range(v + 1)]  # 그래프 초기화
    
    for i in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
        
    result = []
    result = topological_sort(v, indegree, graph, result)
    
    print("위상 정렬 결과:", end = '')
    for node in result:
        print(node, end=' ')
    print()
    
def topological_sort(v, indegree, graph, result):
    queue = deque()
    
    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return result

#-------------------------------------------------------------------
# Ex 7. Team Formation Problem
#-------------------------------------------------------------------
def team_formation_problem():
    # 특정 원소가 속한 집합을 찾기
    n, m = map(int, input().split())
    parent = [0] * (n + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(0, n + 1):
        parent[i] = i


# --------------------------------------------------------------------
# Ex 8. Spilt City
# --------------------------------------------------------------------
def split_city():
    # 노드의 개수와 간선(Union 연산)의 개수 입력받기
    v, e = map(int, input().split())
    parent = [0] * (v + 1) # 부모 테이블 초기화

    # 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
    edges = []
    result = 0


# --------------------------------------------------------------------
# Ex 9. Curriculum Design
# --------------------------------------------------------------------
import copy

def curriculum_design():
    # 노드의 개수 입력받기
    v = int(input())
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (v + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
    graph = [[] for i in range(v + 1)]
    # 각 강의 시간을 0으로 초기화
    time = [0] * (v + 1)


# -------------------------------------------------------------------    
# Main Function Call
# -------------------------------------------------------------------
if __name__ == "__main__":
    main()

    sys.stdin.close()
    sys.stdout.close()