import sys

s = sys.stdin.readline().strip()

a_count = s.count('a')

if a_count == 0 or a_count == len(s):
    print(0)
else:
    s_double = s + s
    window_size = a_count

    first_window = s_double[0:window_size]
    current_b_count = first_window.count('b')

    min_swaps = current_b_count

    for i in range(1, len(s)):
        if s_double[i-1] == 'b':
            current_b_count -= 1
        if s_double[i + window_size - 1] == 'b':
            current_b_count += 1

        if current_b_count < min_swaps:
            min_swaps = current_b_count

    print(min_swaps)