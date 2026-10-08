world = {
    (1, 1): "START",
    (1, 2): "SAFE",
    (1, 3): "PIT",
    (1, 4): "SAFE",
    (2, 1): "SAFE",
    (2, 2): "SAFE",
    (2, 3): "WUMPUS",
    (2, 4): "SAFE",
    (3, 1): "SAFE",
    (3, 2): "SAFE",
    (3, 3): "SAFE",
    (3, 4): "SAFE",
    (4, 1): "SAFE",
    (4, 2): "SAFE", 
    (4, 3): "GOLD",
    (4, 4): "SAFE"
}

path = [(1,1), (2,1), (2,2), (3,2), (3,3), (4,3)]

print("WUMPUS WORLD")

for position in path:

    print("Agent moves to:", position)

    cell = world[position]

    if cell == "START":
        print("Starting position")

    elif cell == "SAFE":
        print("Safe cell")

    elif cell == "PIT":
        print("Agent fell into the pit!")
        print("GAME OVER")
        break

    elif cell == "WUMPUS":
        print("Agent found Wumpus!")
        print("GAME OVER")
        break

    elif cell == "GOLD":
        print("Gold found!")
        print("Mission completed!")
        break