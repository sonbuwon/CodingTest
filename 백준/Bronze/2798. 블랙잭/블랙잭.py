N, M = map(int, input().split())  # 카드 개수 N, 목표 수 M
cards = list(map(int, input().split()))

max_sum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            current_sum = cards[i] + cards[j] + cards[k]

            if current_sum <= M and current_sum > max_sum:
                max_sum = current_sum

print(max_sum)