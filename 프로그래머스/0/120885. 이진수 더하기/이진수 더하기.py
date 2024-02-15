def solution(b1, b2):
    b1 = int(b1, 2)
    b2 = int(b2, 2)

    result = b1 + b2
    result = bin(result)

    return str(result)[2:]