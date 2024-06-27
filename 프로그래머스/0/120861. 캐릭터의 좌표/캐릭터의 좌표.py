def solution(keyinput, board):
    coords = [0, 0]

    x_min = -(board[0] // 2)
    x_max = board[0] // 2
    y_min = -(board[1] // 2)
    y_max = board[1] // 2

    for key in keyinput:
        if key == "left":
            if x_min < coords[0]:
                coords[0] = coords[0] - 1
        elif key == "right":
            if x_max > coords[0]:
                coords[0] = coords[0] + 1
        elif key == "up":
            if y_max > coords[1]:
                coords[1] = coords[1] + 1
        elif key == "down":
            if y_min < coords[1]:
                coords[1] = coords[1] - 1

    answer = coords
    return answer