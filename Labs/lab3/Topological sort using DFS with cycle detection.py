# Implemention of topological sort using DFS with cycle detection
def topologicalSortUtil(v, adj, visited, recStack, stack):
    visited[v] = True
    recStack[v] = True  # Mark current node in recursion stack

    for neighbor in adj[v]:
        if not visited[neighbor]:
            if not topologicalSortUtil(neighbor, adj, visited, recStack, stack):
                return False
        elif recStack[neighbor]:
            # Cycle detected
            return False

    recStack[v] = False  # Remove the node from recursion stack
    stack.append(v)
    return True

def topologicalSort(adj, v):
    stack = []
    visited = [False] * v
    recStack = [False] * v

    for i in range(v):
        if not visited[i]:
            if not topologicalSortUtil(i, adj, visited, recStack, stack):
                print("Cycle detected. Topological sort not possible.")
                return

    print("Topological sorting of graph: ", end="")
    while stack:
        print(stack.pop(), end=" ")

v = 6
edges = [[5, 0], [4, 0], [4, 1], [3, 1], [2, 3], [5, 2]]
adj = [[] for _ in range(v)]
for u, w in edges:
    adj[u].append(w)

topologicalSort(adj, v)

# For another graph with cycle
print("\n")
print("For another graph with cycle 0->1->2->0 \n")

v1=3
edges_two=[[0,1],[1,2],[2,0]]
adj2=[ [] for _ in range(v)]
for u1,w1 in edges_two:
    adj2[u1].append(w1)
topologicalSort(adj2,v1)
