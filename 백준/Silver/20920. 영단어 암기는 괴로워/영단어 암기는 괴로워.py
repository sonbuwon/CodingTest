import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = {}
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

sorted_words = sorted(words.keys(), key=lambda x : (-words[x], -len(x), x))

for s in sorted_words:
    print(s)