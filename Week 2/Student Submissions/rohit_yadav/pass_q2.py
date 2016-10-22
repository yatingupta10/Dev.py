
no_of_students = 5
marks = []
for i in range(0, no_of_students):
    print ("enter the marks of", i+1,"student:")
    mark = int(input("=> "))
    marks.append(mark)

for i in marks:
    if i >= 50:
        status = "Pass"
        print ("The student with marks" ,i, "is", status)
    else:
        status = "Fail"
        print ("The student with marks" ,i, "is", status)