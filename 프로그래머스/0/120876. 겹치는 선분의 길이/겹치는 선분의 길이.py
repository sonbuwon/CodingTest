def solution(lines):
    line_range = [0] * 201

    for line in lines:
        start, end = line
        start += 100
        end += 100
        for i in range(start, end):
            line_range[i] += 1

    overlap_length = 0
    for count in line_range:
        if count > 1:
            overlap_length += 1

    return overlap_length