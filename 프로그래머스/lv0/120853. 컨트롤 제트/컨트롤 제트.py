def solution(s):
    answer = 0
    s = s.split(" ")
    for x in range(len(s)):
        if s[x] == 'Z':
            answer -= int(s[x-1])
        else:
            answer += int(s[x])
    return answer