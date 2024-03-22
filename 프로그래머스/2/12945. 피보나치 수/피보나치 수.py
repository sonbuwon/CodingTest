def solution(n):
    numList = []
    numList.append(0)
    numList.append(1)
    for i in range(2, n+1):
        numList.append(numList[i-2] + numList[i-1])

    return numList[n] % 1234567