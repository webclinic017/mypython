import random

target=random.randint(0,1024)
flag=False
def binaryserach(list1,target):
    count,l,r=0,0,len(list1)-1
    while (l<r-1):
        temp=list1[r-(r-l)/2]
        count+=1
        if temp==target:
            print "round "+str(count)+" AI got the number"
            print "the target number is "+str(target)
            return
        elif temp<target:
            print "round " + str(count) + " number "+str(temp)+" too small"
            l=r-(r-l)/2
        else:
            print "round " + str(count) + " number "+str(temp)+ " too big"
            r=r-(r-l)/2
    return
print "PC:I just picked up one number ,please figure it our what it is"
print "AI starts working to find out "+str(target)
binaryserach(range(1024),target)