graph1 = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}
def dfs(graph, node, visited):   # method is created
    if node not in visited:      # check if node is not visited in stack (if conditon is true -> statement)
        visited.append(node)     #statement which add node in stack 
        for n in graph[node]:       
            dfs(graph, n , visited)      
    return visited               # return visited which return below      
visited = dfs(graph1,'5', [])     #giving value to parameter graph data starting A or visited until stack is empty
print(visited)


