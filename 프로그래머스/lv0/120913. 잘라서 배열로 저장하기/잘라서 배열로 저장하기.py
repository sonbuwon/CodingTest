def solution(my_str, n):
    answer = []

    if len(my_str) % n == 0:
        count = len(my_str) // n
    else:
        count = len(my_str) // n + 1
        
    begin = 0
    end = n
    for i in range(count):
        if i != count - 1:
            answer.append(my_str[begin:end])
            begin+=n
            end+=n
        else:
            answer.append(my_str[begin:])
    
    return answer