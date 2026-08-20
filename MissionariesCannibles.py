from collections import deque

queue=deque([(3,3,0)])

visited=set()

while queue:

    node=queue.popleft()

    if node not in visited:

        print(node,end=" ")

        visited.add(node)

        m,c,boat=node

        if node==(0,0,1):
            print("\nGoal!!")
            break

        neighbours=[]

        moves=[(1,0),(2,0),(0,1),(0,2),(1,1)]

        for x,y in moves:

            if boat==0:
                new=(m-x,c-y,1)

            else:
                new=(m+x,c+y,0)

            nm,nc,nb=new

            if nm<0 or nc<0 or nm>3 or nc>3:
                continue

            if nm>0 and nm<nc:
                continue

            if 3-nm>0 and 3-nm<3-nc:
                continue

            neighbours.append(new)

        for neighbour in neighbours:

            if neighbour not in visited:

                queue.append(neighbour)