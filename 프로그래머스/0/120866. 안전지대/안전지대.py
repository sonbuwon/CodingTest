def solution(board):
    n = len(board)

    directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                        board[nx][ny] = 2

    answer = 0

    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                answer += 1

    return answer