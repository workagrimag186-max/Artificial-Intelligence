from collections import deque

queue=deque([(0,0)]) #queue=dequeu([start])

visited=set()

while queue:

    node=queue.popleft()

    if node not in visited:

        print(node,end=" ")

        visited.add(node)

        a,b=node

        if a==2:
            print("\nGoal reached!")
            break

        neighbours=[]

        # Fill 6L jug
        neighbours.append((6,b))

        # Fill 5L jug
        neighbours.append((a,5))

        # Empty 6L jug
        neighbours.append((0,b))

        # Empty 5L jug
        neighbours.append((a,0))

        # Pour 6L -> 5L
        amount=min(a,5-b)
        neighbours.append((a-amount,b+amount))

        # Pour 5L -> 6L
        amount=min(b,6-a)
        neighbours.append((a+amount,b-amount))

        for neighbour in neighbours:

            if neighbour not in visited:

                queue.append(neighbour)