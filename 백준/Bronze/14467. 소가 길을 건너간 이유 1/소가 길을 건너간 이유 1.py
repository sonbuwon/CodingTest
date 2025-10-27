N = int(input())

cow_info = {}
count = 0

for _ in range(N):
    cow_num, cow_pos = map(int, input().split())

    if cow_num not in cow_info:
        cow_info[cow_num] = cow_pos
    else:
        if cow_info[cow_num] != cow_pos:
            count += 1
            cow_info[cow_num] = cow_pos

print(count)