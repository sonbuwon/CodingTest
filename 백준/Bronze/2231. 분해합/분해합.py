def get_digit_sum(num):
    result = 0
    while num > 0:
        result += num % 10
        num //= 10

    return result

def get_decomposition_sum(num):
    return num + get_digit_sum(num)

def find_smallest_constructor_brute_force(num):
    for i in range(1, num):
        if get_decomposition_sum(i) == num:
            return i

    return 0

N = int(input())
print(find_smallest_constructor_brute_force(N))