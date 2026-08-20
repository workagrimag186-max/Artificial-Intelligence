import heapq
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
heuristic={
    'S':6,
    'A':4,
    'B':5,
    'C':2,
    'D':3,
    'E':4,
    'F':1,
    'G':0
}
queue=[(heuristic['S'],'S')]
visited=set()
while queue:
    _ ,node=heapq.heappop(queue)
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        if node=='G':
            print("\nGoal!!")
            break
        neighbours=[]
        for neighbour in graph[node]:
            if neighbour not in visited:
                neighbours.append(neighbour)
        for neighbour in neighbours:
            heapq.heappush(queue,(heuristic[neighbour],neighbour))
