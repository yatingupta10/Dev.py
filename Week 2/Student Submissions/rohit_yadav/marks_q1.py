
TheoryMarks=int(input('Enter Theory Marks: '))
PracticalMarks=int(input('Enter Practical Marks: '))

if TheoryMarks >= 50:
    print ("Passed in Theory")
else:
    print ("Failed in Theory")
    

if PracticalMarks >= 50:
    print ("Passed in Practical")
else:
    print ("Failed in Practical")
    

if (TheoryMarks + PracticalMarks >= 140):
    print ("Passed Overall")
else:
    print ("Failed Overall")