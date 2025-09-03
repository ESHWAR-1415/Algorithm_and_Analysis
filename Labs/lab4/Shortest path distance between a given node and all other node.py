 # Implementation of DFS to find shortest path distance between a given node and all other node
def dfs_shortest_path(graph,start):
    distance={}
    current_layer=[start]
    next_layer=[]
    distance[start]=0
    while(current_layer):
        current_node=current_layer.pop(0)
        for neighbor in graph[current_node]:
            if neighbor not in distance:
                next_layer.append(neighbor)
                distance[neighbor]=distance[current_node]+1
        if neighbor not in current_layer:
            current_layer,next_layer = next_layer,[]
    return distance
graph={
    'A':['B','D'],
    'B':['A','C'],
    'C':['B','G'],
    'D':['A','E'],
    'E':['D','F'],
    'F':['E','G'],
    'G':['H','I','C','F'],
    'H':['G','I'],
    'I':['G','H']
    }
dist_path = dfs_shortest_path(graph,'A')
print(dist_path)
