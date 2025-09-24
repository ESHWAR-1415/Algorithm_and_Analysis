from collections import deque
INF =float('inf')
NIL = -1
def bfs(adj,pair_U,pair_V,dist,m):
    queue = deque()
    for u in range(m):
        if pair_U[u]==NIL:
            dist[u]=0
            queue.append(u)
        else:
            dist[u]=INF
    found_augmenting_path=False
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if pair_V[v]==NIL:
                found_augmenting_path=True
            elif dist[pair_V[v]]==INF:
                dist[pair_V[v]]=dist[u]+1
                queue.append(pair_V[v])
    return found_augmenting_path
def dfs(u,adj,pair_U,pair_V,dist):
    for v in adj[u]:
        stmt1 = (pair_V[v])==NIL
        stmt2=(dist[pair_V[v]]==dist[u]+1 and dfs(pair_V[v],adj,pair_U,pair_V,dist))
        if stmt1 or stmt2:
            pair_U[u]=v
            pair_V[v]=u
            return True
    dist[u]=INF
    return False
def hopcroft_karp(m,n,edges):
    adj=[[]for _ in range(m)]
    for u,v in edges:
        adj[u].append(v)
    pair_U = [NIL]*m
    pair_V = [NIL]*n
    dist = [INF]*m
    matching =0
    while bfs(adj,pair_U,pair_V,dist,m):
        for u in range(m):
            if pair_U[u]==NIL and dfs(u,adj,pair_U,pair_V,dist):
                matching +=1
    return matching
    
#example usage
m,n = 3,3
edges = [(0,0),(0,1),(1,0),(2,2)]
print("Maximum matching size:",hopcroft_karp(m,n,edges))
