# Implementation of Kahn's topological sort using BFS
from collections import deque
V=6
edges = [[5, 0], [4, 0], [4, 1],[3, 1], [2, 3], [5, 2]]

def kahns_topologicalsort(V, edges):
  adj = [[] for _ in range(V)]
  in_degree = [0] * V
  for u,v in edges:
    adj[u].append(v)
    in_degree[v] += 1
  print("In degree:", in_degree)
  queue = deque([i for i in range(V) if in_degree[i] == 0])
  top_order = []
  while queue:
    u = queue.popleft()
    top_order.append(u)
    for neighbor  in adj[u]:
      in_degree[neighbor] -= 1
      if in_degree[neighbor]==0:
        queue.append(neighbor)
  if len(top_order) == V:
    return top_order
  else:
    return "graph has a cycle, topological sort not possible."
result = kahns_topologicalsort(V, edges)
print("topological sort order", result)
