def solution(polynomial):
    temp1 = 0
    temp2 = 0

    for value in polynomial.split(" + "):
        if value[-1] == "x":
            if len(value) >= 2:
                temp1 = temp1 + int(value[0:-1])
            else:
                temp1 = temp1 + 1
        else:
            temp2 = temp2 + int(value)

    answer = []

    if temp1 > 0:
        if temp1 == 1:
            answer.append("x")
        else:
            answer.append(f"{temp1}x")
    
    if temp2 > 0:
        answer.append(f"{temp2}")

    return " + ".join(answer)