score_chart = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

subjectCount = 20

total = 0.0
gradeTotal = 0.0

for x in range(subjectCount):
    subject, grade, score = input().split()
    grade = float(grade)
    
    if  score != 'P': 
        score = score_chart[score]
        total += grade * score
        gradeTotal += grade

print(total / gradeTotal)