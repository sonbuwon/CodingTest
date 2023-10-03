def solution(s):
    temp = []
    for i in sorted(list(set(s))):
        if s.count(i) == 1:
            temp.append(i)

    if len(temp) == 0:
        return ""
    else:
        return ''.join(temp)