def solution(sides):
    a, b = sides
    max_side = a + b - 1
    min_side = abs(a - b) + 1

    answer = max_side - min_side + 1
    return answer