N = int(input())
records = []
total_count = 0

for _ in range(N):
    num, loc = map(int, input().split())
    records.append([num, loc])

cow_nums = set()
for record in records:
    cow_nums.add(record[0])
    
for cow_num in cow_nums:
    isFirst=True
    now_posi = []
    for record in records:
        if record[0] == cow_num and isFirst == True:
            isFirst = False
            now_posi = [record[0], record[1]]
        if record[0] == cow_num and record[1] != now_posi[1] and isFirst == False:
            total_count+=1
            now_posi = [record[0], record[1]]
            
print(total_count)