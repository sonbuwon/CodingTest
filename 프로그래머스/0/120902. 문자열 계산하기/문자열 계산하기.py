def solution(s):
    elements = s.split(' ')
    result = int(elements[0])


    for i in range(1, len(elements) - 1, 2):
        operator = elements[i]
        next_number = elements[i+1]

        if operator == '+':
            result += int(next_number)
        elif operator == '-':
            result -= int(next_number)

    return result