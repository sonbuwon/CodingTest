maxValue = 0
maxiIndex = 0
maxjIndex = 0

for i in range(9):
    line = list(map(int, input().split()))
    lineMax = max(line)

    if lineMax > maxValue:
        maxValue = lineMax
        maxiIndex = i
        maxjIndex = line.index(lineMax)

print(maxValue)
print(maxiIndex+1, maxjIndex+1)