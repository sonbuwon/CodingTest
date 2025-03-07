def solution(participant, completion):
    hash_sum = 0
    
    for p in participant:
        hash_sum += hash(p)
        
    for c in completion:
        hash_sum -= hash(c)
        
    for p in participant:
        if hash(p) == hash_sum:
            return p