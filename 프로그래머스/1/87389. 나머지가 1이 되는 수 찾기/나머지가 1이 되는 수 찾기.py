def solution(n):
    divnum = n - 1
    minValue = divnum
    while divnum > 0:
        if n % divnum == 1:
            minValue = divnum
        
        divnum -= 1
    
    return minValue