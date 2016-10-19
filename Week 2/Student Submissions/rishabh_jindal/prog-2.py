
class student:
    def __init__(self, prcntge=0):
        self.percentage=prcntge
        if self.percentage>50:
            self.status="Pass"
        else:
            self.status="Fail"

    def getPercentage(self):
        return self.percentage
    def getStatus(self):
        return self.status

obj=[]
for i in range(0,5):
    print "enter percentage of student:",i
    perc=int(raw_input())
    obj.insert(i,student(perc))


k=0
for i in obj:
    print "Student",k
    print i.getStatus()
    print i.getPercentage()
    k+=1
