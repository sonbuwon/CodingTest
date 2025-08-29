rect_xt = []

for _ in range(3):
    rect_xt.append(list(map(int, input().split())))
    
result_x = rect_xt[0][0] ^ rect_xt[1][0] ^ rect_xt[2][0]
result_y = rect_xt[0][1] ^ rect_xt[1][1] ^ rect_xt[2][1]

print(result_x, result_y)