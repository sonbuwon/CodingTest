def solution(n):
    def is_three_related(number):
        return number % 3 == 0 or '3' in str(number)
    
    count = 0
    current_number = 0

    while count < n:
        current_number += 1
        if not is_three_related(current_number):
            count += 1
        
    return current_number