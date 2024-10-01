# 변수 선언 및 입력
N = int(input())
x, y = 0, 0

# 동, 서, 남, 북 순으로 dx, dy를 정의
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

move_dir = {
    'E' : 0,
    'W' : 1,
    'S' : 2,
    'N' : 3
}

# 움직이는 것을 진행
for _ in range(N):
    c_dir, dist = tuple(input().split())
    dist = int(dist)
    
    # 주어진 방향대로 dist 거리만큼 이동했을 경우의 위치 계산
    x += dx[move_dir[c_dir]] * dist
    y += dy[move_dir[c_dir]] * dist

print(x, y)