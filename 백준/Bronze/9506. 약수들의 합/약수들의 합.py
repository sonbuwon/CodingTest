while(True):
    n = int(input())
    list = []

    if n == -1:
        break;

    for i in range(n-1):
        if n % (i+1) == 0:
            list.append(i+1)

    total = 0
    for i in list:
        total += i

    if total == n:
        print(f'{n} = ', end='')
        for i in list:
            if i == list[-1]:
                print(f'{i}')
            else:
                print(f'{i} + ', end='')
    else:
        print(f'{n} is NOT perfect.')