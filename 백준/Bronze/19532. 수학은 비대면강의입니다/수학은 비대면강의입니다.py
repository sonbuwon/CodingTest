a, b, c, d, e, f = map(int, input().split())

found = False
for x in range(-999, 1000):
    if found:
        break
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            found = True
            print(x, y)
            break