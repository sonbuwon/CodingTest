def solution(phone_book):
    hash_set = set(phone_book)
    for phone in hash_set:
        prefix = ""
        for p in phone:
            prefix += p
            if prefix in hash_set and prefix != phone:
                return False
    
    return True