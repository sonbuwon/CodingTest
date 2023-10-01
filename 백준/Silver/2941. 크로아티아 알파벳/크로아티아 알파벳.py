c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

t_str = input()

count = 0
for i in c_alpha:
    count += t_str.count(i)
    t_str = ','.join(t_str.split(i))

print(len(''.join(t_str.split(','))) + count)