def is_acceptable(password):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    has_vowel = False
    for c in password:
        if c in vowels:
            has_vowel = True

    if not has_vowel:
        return False

    for i in range(len(password) - 2):
        three_chars = password[i:i+3]
        vowel_count = sum(1 for c in three_chars if c in vowels)
        if vowel_count == 3 or vowel_count == 0:
            return False
        
    for i in range(len(password) - 1):
        if password[i] == password[i+1]:
            if password[i:i+2] not in ['ee', 'oo']:
                return False

    return True

while True:
    password = input().strip()

    if password == 'end':
        break

    if is_acceptable(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")