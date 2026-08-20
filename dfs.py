graph={
    2: [0,1,6],
    1: [0,7,4,2],
    0:[7,1,2,3],
    3:[0,5],
    6:[2,4],
    4:[1,6],
    5:[3],
    7:[0,1]
}
stack=[2]
visited=set()
while stack:
    node=stack.pop()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)