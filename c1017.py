#10월 17일 DFS/BFS

def main():
    print("10월 17일. DFS/BFS")
    gcdfn(192,162)
    dfs(graph, 1, visited)
    bfsFn()
    
def gcdfn(a,b):
    
    if a > b:
        pass
    else: 
        a,b = b,a #값 교체
        
    GCD = gcd(a,b)
    print(f"{a}, {b}, 최대공약수 {GCD}")
        
def gcd(a,b):
    if a % b == 0:
        return b
    else: 
        return gcd(b, a%b)

    
def dfs(graph, v, visited):
    visited[v] =True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],    
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
    
visited = [False] * 9
    
dfs(graph, 1, visited)
            
            
def bfsFn():
    visited = [False] * 9
    print("\n-- BFS --:", end='')
    bfs(1, visited)
    
from collections import deque
def bfs(start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    

if __name__ == "__main__":
    main()