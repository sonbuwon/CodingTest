word = input()

is_palindrome = True

for i in range(len(word)//2):
    if word[i] != word[-(i+1)]:
        is_palindrome = False
        break

print(1 if is_palindrome==True else 0)