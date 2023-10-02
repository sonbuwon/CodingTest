num = int(input())
count = 0

for x in range(num):
    temp_str = input()

    list1 = []
    list2 = []
    for i in range(len(temp_str)):
        if i == 0:
            list1.append(temp_str[i])
        elif list1.count(temp_str[i]) == 0 or (temp_str[i] == temp_str[i-1]):
            list1.append(temp_str[i])
        else:
            list2.append(temp_str[i])
    
    if len(list2) == 0:
        count+=1

print(count)