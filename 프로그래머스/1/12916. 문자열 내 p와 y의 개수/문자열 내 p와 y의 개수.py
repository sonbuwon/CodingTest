def solution(s):
    pList =[]
    yList = []
    s = s.lower()

    for i in s:
        if i == 'p':
            pList.append(i)
        elif i == 'y':
            yList.append(i)

    if len(pList) == len(yList):
        return True
    else:
        return False