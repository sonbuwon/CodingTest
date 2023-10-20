import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

prefix_sum = [0]
temp = 0

for i in N_list:
    temp = temp + i
    prefix_sum.append(temp)

for x in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])