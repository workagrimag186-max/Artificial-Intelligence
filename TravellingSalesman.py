import heapq

graph={

    'A':{'B':10,'C':15,'D':20},

    'B':{'A':10,'C':35,'D':25},

    'C':{'A':15,'B':35,'D':30},

    'D':{'A':20,'B':25,'C':30}

}

queue=[(0,'A')]

visited=set()

total=0

while queue:

    distance,node=heapq.heappop(queue)

    if node not in visited:

        print(node,end=" ")

        visited.add(node)

        total=total+distance

        neighbours=[]

        for neighbour in graph[node]:

            if neighbour not in visited:

                neighbours.append(neighbour)

        for neighbour in neighbours:

            heapq.heappush(queue,(graph[node][neighbour],neighbour))

print("\nTotal Cost:",total)