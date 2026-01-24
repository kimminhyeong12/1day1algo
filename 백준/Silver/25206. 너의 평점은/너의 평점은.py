subject = []
credit = []
grade = []
credit_result = 0
grade_result = 0
for i in range(20):
    list_input = list(input().split())
    subject.append(list_input[0])
    credit.append(list_input[1])
    grade.append(list_input[2])
for k in range(20):
    if grade[k] == "A+":
        grade[k] = 4.5
    elif grade[k] == "A0":
        grade[k] = 4.0
    elif grade[k] == "B+":
        grade[k] = 3.5
    elif grade[k] == "B0":
        grade[k] = 3.0
    elif grade[k] == "C+":
        grade[k] = 2.5
    elif grade[k] == "C0":
        grade[k] = 2.0
    elif grade[k] == "D+":
        grade[k] = 1.5
    elif grade[k] == "D0":
        grade[k] = 1.0
    elif grade[k] == "F":
        grade[k] = 0
    elif grade[k] == "P":
        continue
    credit_result += float(credit[k])
    grade_result += grade[k] * float(credit[k])
print(grade_result / credit_result)