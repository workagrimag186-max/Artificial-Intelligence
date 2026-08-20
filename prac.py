from collections import deque
queue=deque([(0,0)])
visited=set()
while queue:
    node=queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        a,b=node
        neighbours=[]
        if b==3:
            print("\n Goal!!")
            break
        neighbours.append((5,b))
        neighbours.append((a,4))
        neighbours.append((0,b))
        neighbours.append((a,0))
        amount= min(a,4-b)
        neighbours.append((a-amount, b+amount))
        amount=min(b,5-a)
        neighbours.append((a+amount,b-amount))

        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)