#Implemetation of topological sort using DFS without cycle detection
def topologicalSortutil(v,adj,visited,stack):
  visited[v] = True
  for i in adj[v]:
    if not visited[i]:
      topologicalSortutil(i, adj, visited, stack)
  stack.append(v)

def topologicalsort(adj,v):
  stack=[]
  visited=[False]*v
  for i in range(v):
    if not visited[i]:
      topologicalSortutil(i,adj,visited,stack)
  print("Topological sorting of graph: ",end="")
  while stack:
    print(stack.pop(),end=" ",)
  
    

v=6
edges = [[5, 0], [4, 0], [4, 1],[3, 1], [2, 3], [5, 2]]
adj=[[]for _ in range(v)]
for i in edges:
  adj[i[0]].append(i[1])
topologicalsort(adj,v)

# For another graph with cycle
print("\n")
v1=3
edges_two=[[0,1],[1,2],[2,0]]
adj2=[ [] for _ in range(v)]
for i in edges_two:
    adj2[i[0]].append(i[1])
topologicalsort(adj2,v1)
