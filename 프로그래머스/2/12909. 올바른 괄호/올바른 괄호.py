def solution(s):
    answer = True
    temp_stack = []
    
    for i in s:
    # print(i)
        if i == '(':
            temp_stack.append(i)
        elif i == ')':
            if len(temp_stack) == 0:
                # 닫힌 괄호 인데 스택이 비었다면 균형을 이루지 않는다는 것
                answer = False
                break 

            temp_stack.pop()

    if answer != False and len(temp_stack) == 0:
        answer = True
    else:
        answer = False

    return answer