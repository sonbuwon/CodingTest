n = int(input())
numList = list(map(int, input().split()))

sosu = 0
for num in numList:
    count = 0
    if num != 1:
        for x in range(2, num+1):
            if num % x == 0:
                count += 1

    if count == 1:
        sosu+=1

print(sosu)