def solution(numList, n):
    return sorted(numList, key= lambda x :(abs(x - n), -x))