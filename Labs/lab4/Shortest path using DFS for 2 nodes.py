# Implementing shortest path using dfs for start and end node
def dfs_shortest_path(graph, start, end, path=None, visited=None, shortest=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    # If we reached the end node
    if start == end:
        if shortest is None or len(path) < len(shortest):
            shortest = path.copy()
    else:
        for neighbor in graph[start]:
            if neighbor not in visited:
                shortest = dfs_shortest_path(graph, neighbor, end, path, visited, shortest)

    # Backtrack
    path.pop()
    visited.remove(start)

    return shortest

# Example graph as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

start_node = 'A'
end_node = 'G'

shortest_path = dfs_shortest_path(graph, start_node, end_node)
print("Shortest path:", shortest_path)
