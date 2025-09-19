N = int(input())
people = []
rank_info = [0] * N
for _ in range(N):
    w, h = map(int, input().split())
    people.append([w, h])
    
for i, person in enumerate(people):
    rank = 1
    for j, p in enumerate(people):
        if i != j:
            if person[0] < p[0] and person[1] < p[1]:
                rank += 1
    
    rank_info[i] = rank
    
for rank in rank_info:
    print(rank, end=' ')