rows = int(input())
col = int(input())
grid = []
instructions = []
for i in range(rows):
    hold = list(input())
    grid.append(hold)

tasks = int(input())

for i in range(tasks):
    hold = input()
    instructions.append(hold)

def forward(whichlist, here, direction):
    if direction == 0:
        whichlist -= 1
    elif direction == 1:
        here += 1
    elif direction == 2:
        whichlist += 1
    else:
        here -= 1
    return [whichlist, here, direction]

def left(direction):
    if direction == 0:
        direction = 3
    elif direction == 3:
        direction = 2
    elif direction == 2:
        direction = 1
    else:
        direction = 0
    return direction

def right(direction):
    if direction == 0:
        direction = 1
    elif direction == 1:
        direction = 2
    elif direction == 2:
        direction = 3
    else:
        direction = 0
    return direction

final = []

for i in range(rows):

    for x in range(col):

        for p in range(4):
            first = i
            second = x
            facing = p
            for z in instructions:

#                print(first)
#                print(second)
#                print(facing)
#                print(z)
                if first > rows - 1 or first < 0 or second > col -1 or second < 0 or grid[first][second] == "X":
#                    print('here')
                    break
                if z == "F":
                    save = forward(first, second, facing)
                    first = save[0]
                    second = save[1]
                elif z == "L":
                    facing = left(facing)
                else:
                    facing = right(facing)
            if z == instructions[-1]:
                if first < rows and first > -1 and second < col and second > -1 and grid[first][second] == ".":
#                    print(i, x, p)
#                    print("adding")
                    final.append([first,second])

for i in final:
    grid[i[0]][i[1]] = '*'

for i in grid:
    print(*i, sep="")

