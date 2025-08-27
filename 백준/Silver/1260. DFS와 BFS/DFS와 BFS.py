from collections import deque

def dfs(graph, start, visited, result):
    visited[start] = True
    result.append(start)
    
    # 인접한 정점들을 작은 번호부터 방문
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)

def bfs(graph, start):
    visited = [False] * (len(graph))
    result = []
    queue = deque([start])
    visited[start] = True
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        # 인접한 정점들을 작은 번호부터 큐에 추가
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result

# 입력 받기
N, M, V = map(int, input().split())

# 그래프 초기화 (인덱스 0은 사용하지 않음)
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 정점의 인접리스트를 정렬 (작은 번호부터 방문하기 위해)
for i in range(1, N + 1):
    graph[i].sort()

# DFS 수행
visited_dfs = [False] * (N + 1)
dfs_result = []
dfs(graph, V, visited_dfs, dfs_result)

# BFS 수행
bfs_result = bfs(graph, V)

# 결과 출력
print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))