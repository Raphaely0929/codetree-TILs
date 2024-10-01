c = input()
x, y = 0, 0
dir = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in c:
    if i == 'L':
        dir = (dir + 3) % 4
    elif i == 'R':
        dir = (dir + 1) % 4
    elif i == 'F':
        x += dx[dir]
        y += dy[dir]

print(x, y)