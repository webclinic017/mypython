import random

target=random.randint(0,1000)
print "PC:I just picked up one number ,please figure it out what it is"
flag=False
count=0
while (flag==False):
    inputnum=int(input("please input the number: "))
    count+=1
    if inputnum>target:print "not correct ,too big"
    elif inputnum<target:print "not correct ,too small"
    else:
        flag=True
        print "Congrats,you got the number "  +",you used "+str(count)+" rounds"
