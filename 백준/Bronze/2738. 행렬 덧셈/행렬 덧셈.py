n,m = map(int, input().split())

a = []
b = []

for i in range(n):
    line = list(input().split())
    a.append(line)

for i in range(n):
    line = list(input().split())
    b.append(line)

for i in range(n):
    for j in range(m):
        a[i][j] = int(a[i][j]) + int(b[i][j])
        print(a[i][j], end=" ")
    print()