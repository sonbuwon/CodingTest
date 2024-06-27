def solution(dots):
    x_coords = [dot[0] for dot in dots]
    y_coords = [dot[1] for dot in dots]

    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)

    answer = (y_max - y_min) * (x_max - x_min)

    return answer