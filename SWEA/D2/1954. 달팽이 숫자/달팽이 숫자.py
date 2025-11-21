T = int(input())

for t in range(1, T + 1):
    N = int(input())
    if N < 1 or N > 10:
        raise ValueError("N은 1 이상 10 이하이어야 합니다.")

    snail = [[0]*N for _ in range(N)]

    dx = [0, 1, 0, -1]  # 오른, 아래, 왼, 위
    dy = [1, 0, -1, 0]

    x, y, d = 0, 0, 0   # 시작 위치 & 방향(오른쪽)
    for num in range(1, N*N + 1):
        snail[x][y] = num

        nx = x + dx[d]
        ny = y + dy[d]

        # 배열 벗어나거나 이미 값이 있으면 방향 전환
        if nx < 0 or nx >= N or ny < 0 or ny >= N or snail[nx][ny] != 0:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        x, y = nx, ny

    print(f"#{t}")
    for row in snail:
        print(*row)