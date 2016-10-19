TheoryMarks=int(raw_input('Enter Theory Marks: '))
PracticalMarks=int(raw_input('Enter Practical Marks: '))

if TheoryMarks>50:
    print "Passed in Theory"
    pass
else:
    print "Failed in Theory"
    pass

if PracticalMarks>50:
    print "Passed in Practical"
    pass
else:
    print "Failed in Practical"
    pass

if(TheoryMarks>50 and PracticalMarks>50):
    print "Passed Overall"
    pass
else:
    print "Failed Overall"
