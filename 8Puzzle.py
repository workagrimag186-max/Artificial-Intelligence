from collections import deque

queue=deque([
    (1,2,3,4,0,6,7,5,8)
])

visited=set()

while queue:

    node=queue.popleft()

    if node not in visited:

        print(node, end=" ")

        visited.add(node)

        if node==(1,2,3,4,5,6,7,8,0):
            print("\nGoal!!")
            break

        zero=node.index(0)

        neighbours=[]

        # Move blank UP
        if zero>=3:
            new=list(node)
            new[zero],new[zero-3]=new[zero-3],new[zero]
            neighbours.append(tuple(new))

        # Move blank DOWN
        if zero<6:
            new=list(node)
            new[zero],new[zero+3]=new[zero+3],new[zero]
            neighbours.append(tuple(new))

        # Move blank LEFT
        if zero%3!=0:
            new=list(node)
            new[zero],new[zero-1]=new[zero-1],new[zero]
            neighbours.append(tuple(new))

        # Move blank RIGHT
        if zero%3!=2:
            new=list(node)
            new[zero],new[zero+1]=new[zero+1],new[zero]
            neighbours.append(tuple(new))

        for neighbour in neighbours:

            if neighbour not in visited:

                queue.append(neighbour)