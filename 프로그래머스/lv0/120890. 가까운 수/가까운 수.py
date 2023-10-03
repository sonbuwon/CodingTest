def solution(array, n):
    answer = 0
    array = sorted(array)
    tempList = []
    for i in array:
        tempList.append(abs(n-i))
    
    answer = array[tempList.index(min(tempList))]
    return answer

print(solution([1,100,98], 99))