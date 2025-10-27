H, W = map(int, input().split())

answer = [[0]*W for _ in range(H)]

for i in range(H):
    weather_row = input().strip()
    cloud_counter = -1

    for j in range(W):
        if weather_row[j] == 'c':
            cloud_counter = 0
            answer[i][j] = 0
        elif weather_row[j] == '.' and cloud_counter != -1:
            cloud_counter += 1
            answer[i][j] = cloud_counter
        else:
            answer[i][j] = -1

for row in answer:
    print(*row)