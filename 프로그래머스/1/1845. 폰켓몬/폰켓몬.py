def solution(nums):
    
    # 선택 할 수 있는 폰켓몬 수
    n_half = len(nums) // 2
    
    # 중복 제거한 고유 폰켓몬 종류 수
    unique_types = len(set(nums))
    
    answer = min(n_half, unique_types)
    
    return answer