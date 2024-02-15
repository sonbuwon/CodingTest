def solution(quiz):
    answer = []

    for i in quiz:
        l = i.split(' ')
        if l[1] == '+':
            if int(l[-1]) == (int(l[0]) + int(l[2])):
                answer.append("O")
            else:
                answer.append("X")
            
        elif l[1] == '-':
            if int(l[-1]) == (int(l[0]) - int(l[2])):
                answer.append("O")
            else:
                answer.append("X")
                
    return answer