#Implementating shortest distance from given start node to end node using BFS
def shortest_path(graph, start, end):
    queue =([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        node, distance = queue.pop()

        if node == end:
            return distance

        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
                    visited.add(neighbor)

    return -1

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['E', 'F', 'B', 'A'],
    'D': ['B'],
    'E': ['C'],
    'F': ['C']
}

start = 'A'
end = 'F'

path_length = shortest_path(graph, start, end)
print(f"The shortest path length from {start} to {end} is: {path_length}")
