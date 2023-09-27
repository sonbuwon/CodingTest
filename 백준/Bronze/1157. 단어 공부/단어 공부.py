word = input()
wordSetList = sorted(list(set(word.lower())))

countList = []
for i in wordSetList:
    countList.append(word.lower().count(i))

if countList.count(max(countList)) > 1:
    print('?')
else:
    print(wordSetList[countList.index(max(countList))].upper())