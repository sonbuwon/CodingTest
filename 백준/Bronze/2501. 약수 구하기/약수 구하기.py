N, K = map(int, input().split())

list = []
count = 0
for i in range(N):
    if N % (i+1) == 0:
        list.append(i+1)
        count+=1

if count < K:
    print(0)
else:
    print(list[K-1])