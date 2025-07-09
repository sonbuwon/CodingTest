def solution(sizes):
    
    max_sides = []
    min_sides = []

    for w, h in sizes:
        max_sides.append(max(w, h))
        min_sides.append(min(w, h))

    return max(max_sides) * max(min_sides)