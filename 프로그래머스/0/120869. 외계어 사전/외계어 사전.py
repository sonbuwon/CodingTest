def solution(spell, dic):
    spell_word = ''.join(sorted(spell))

    for word in dic:
        if ''.join(sorted(word)) == spell_word:
            return 1
        
    return 2