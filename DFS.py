def dfs(graph, src, visited):    
    if src not in visited:
        #dfs_traversal_list.append(src)
        print(src,"=>",end='')
        visited.add(src)

        for adj_node in graph[src]:
            dfs(graph, adj_node, visited)

  



if __name__=="__main__":
    visited = set()
    dfs_traversal_list = list()

    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }

    dfs(graph, 'A', visited)
