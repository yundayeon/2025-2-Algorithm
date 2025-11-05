#10월 31일 dfs, bfs 예제, 정렬
import sys

sys.stdin = open('input.txt', encoding="utf-8")
# sys.stdout = open('output.txt','w', encoding="utf-8" )
sys.stdout = open('output.txt','a', encoding="utf-8" )

from collections import deque

Debug = 0 # 토글 스위치, 디버그 모드 0:OFF, 1:ON

def dfs(x,y,n,m,graph):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상,하,좌,우의 위치들도 모두 재귀적으로 호출
        #2. 수학에서 사용하는 좌표와 프로그래밍에서 사용하는 좌표는 다름(행렬 개념)
        dfs(x-1,y,n,m,graph)
        dfs(x,y-1,n,m,graph)
        dfs(x+1,y,n,m,graph)
        dfs(x,y+1,n,m,graph)
        return True
    return False

def iceFn():
    n, m = map(int, input().spilit())
    # graph = []
    # for i in range(n):
    # graph.append(list(map(int, input().rstrip())) #***
    graph = [list(map(int, input().rstrip())) for _ in range(n)]
    
    # print(n , m)
    # print(graph)
    
    result = 0 
    for i in range(n):
        for j in range(m):
            # 그래프는 리스트
            # 1.리스트를 함수의 변수로 넘길 떄는 주소가 넘어감(참조 전달)
            if dfs(i,j,n,m,graph):
                result += 1
                
    print(f"얼음조각 갯수 : {result}")
    
def mazeFn():
    n,m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    
    # BFS 소스코드 구현
    def bfs(x,y): # sum += i   sum(ListName)
        # 큐 구현을 위해 deque 라이브러리 사용
        MyQueue = deque()
        MyQueue.append((x,y))
        #큐가 빌 때까지 반복하기
        while MyQueue:
            x,y = MyQueue.popleft()
            # 현재 위치에서 네 방향으로 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 미로 찾기 공간을 벗어난 경우 무시
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                # 벽인 경우 무시
                if graph[nx][ny] == 0:
                    continue
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    MyQueue.append((nx,ny))
        # 가장 오른쪽 아래까지의 최단 거리 반환
        return graph[n-1][m-1]
    
def sortingIndexFn():
    # n = 6
    # # m = 6
    # m = n
    # for i in range(n):
    #     for j in range(m):
    #         print(f"({i},{j})", end=' ')
    #     print()
    
    # 작은 값을 앞으로 보내는 정렬

    # [1,7,6,3,9,2] 1회전
    # [1,2,7,6,9,3] 2회전

    # (0,1) (0,2) (0,3) (0,4) (0,5)
    # (1,2) (1,3) (1,4) (1,5)
    # (2,3) (2,4) (2,5)
    # (3,4) (3,5)
    # (4,5)
    # row = n - 1
    # col = n
    
    # for i in range(row):
    #     for j in range(i+1, col):
    #         print(f"({i},{j})", end = ' ')
    #     print()
        
    # for i in range(___):
    #     for j in range(___):
    #         print(f"({__},{___})", end = ' ')
    #     print()
    
    # (0,1) (1,2) (2,3) (3,4) (4,5)
    # (0,1) (1,2) (2,3) (3,4)
    # (0,1) (1,2) (2,3)
    # (0,1) (1,2)
    # (0,1)
    
    # rows = n-1    
    # for row in range(rows):
    #     cols = n - row-1
    #     for col in range(cols):
    #         print(f"{col},{col+1}", end= ' ')
    #     print()
    data = [3,7,6,1,9,2]
    n = len(data)
    rows = n -1
    cols = n
    
    # for row in range(n):
    #     for col in range(row+1, cols):
    #         if(data[row] > data[col]):
    #             data[row], data[col] = data[col], data[row]
    #         print(f"{row+1}회전: {data}")

    for row in range(rows):
        cols = n - row-1
        for col in range(cols):
            if(data[col] > data[col+1]):
                #스왑
                data[col], data[col+1] = data[col+1], data[col]
        print(f'{row+1}회전: {data}')
    print(f"{row+1}회전 정렬 결과: {data}")
    
        # 버블 정렬(Bubble sort) 알고리즘 소스코드
    data = [3,7,6,1,9,2]
    # [3,6,1,7,6,1,9] 1회전
    # [3,1,6,2,7,9] 2회전
    n = len(data)
    


if __name__ == "main":
    print("test")
    iceFn()
    mazeFn()
    sortingIndexFn()
    
    ## if Debug:
    ##     print("Debug Mode")
    ##     sys.stdout = open('output.txt','w', encoding="utf-8" )
        