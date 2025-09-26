N, M = map(int, input().split())
n_set = set()
m_set = set()

for _ in range(N):
    n_set.add(input())

for _ in range(M):
    m_set.add(input())

result = sorted(n_set & m_set)

print(len(result))
for r in result:
    print(r)