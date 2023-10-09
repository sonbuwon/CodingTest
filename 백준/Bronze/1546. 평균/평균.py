n = int(input())
num_list = list(map(int, input().split()))

maxValue = max(num_list)
newList = []
for i in num_list:
    newList.append((i/maxValue) * 100)

print(sum(newList) / n)