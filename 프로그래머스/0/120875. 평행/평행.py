def solution(dots):
    [x1, y1], [x2, y2], [x3, y3], [x4, y4] = dots

    def slope(p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2:
            return float('inf')
        return (y2 - y1) / (x2 - x1)
    
    lines = [
        (slope([x1, y1], [x2, y2]), slope([x3, y3], [x4, y4])),
        (slope([x1, y1], [x3, y3]), slope([x2, y2], [x4, y4])),
        (slope([x1, y1], [x4, y4]), slope([x2, y2], [x3, y3])),
    ]

    for slope1, slope2 in lines:
        if slope1 == slope2:
            return 1
        
    return 0