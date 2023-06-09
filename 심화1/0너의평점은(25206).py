
all = 0.0
count = 0
for _ in range (20):
    A = input().split()
    score, hakk = float(A[1]), A[2]
    if hakk == 'A+':
        all += score * 4.5
        count += score
    elif hakk == 'A0':
        all += score * 4.0
        count += score
    elif hakk == 'B+':
        all += score * 3.5
        count += score
    elif hakk == 'B0':
        all += score * 3.0
        count += score
    elif hakk == 'C+':
        all += score * 2.5
        count += score
    elif hakk == 'C0':
        all += score * 2.0
        count += score
    elif hakk == 'D+':
        all += score * 1.5
        count += score
    elif hakk == 'D0':
        all += score * 1.0
        count += score
    elif hakk == 'F':
        count += score
    else:
        continue
if count == 0:
    print(0.0)
print(format(all / count, ".6f"))

"""

grade_table = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

total_credit = 0
total_score = 0

for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    
    if grade == 'P':
        continue  # P/F 과목은 계산에서 제외
    
    total_credit += credit
    total_score += credit * grade_table[grade]

gpa = total_score / total_credit

print(format(gpa, ".6f"))


"""