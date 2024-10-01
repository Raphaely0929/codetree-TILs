n = int(input())
x, y = 0, 0

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def adj_cnt(x, y):
    cnt = 0

    for dx, dy in zip(dxs, dys):
        x += dx
        y += dy
        if in_range(x,y) and arr[x][y] == 1:
            cnt += 1
    
    return cnt


for i in range(n):
    for j in range(n):
        if adj_cnt(x, y) >= 3:
            ans += 1

print(ans)