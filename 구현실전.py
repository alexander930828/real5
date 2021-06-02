# 입력 값

n = int(input())
plans = map(str, input().split())
x, y = 1, 1

# 상하좌우

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

move_types = ['U', 'D', 'L', 'R']

# 시작점
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나는 경우는 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    #이동 수행
    x, y = nx, ny

print(x, y)