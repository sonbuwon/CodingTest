def solution(s):
    result = 0

    for i in s:
        result += str(i).count('7')

    return result