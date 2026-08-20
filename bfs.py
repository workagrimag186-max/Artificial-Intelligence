from collections import deque
graph={
    'S':['A','B'],
    'A':['C','D'],
    'B':['E'],
    'C':[],
    'D':['F'],
    'E':['G'],
    'F':[],
    'G':[]
}
queue= deque(['S'])
visited=set()
while queue:
    node=queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)