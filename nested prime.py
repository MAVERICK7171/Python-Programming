n=int(input("enter a number"))
count=0
num=n
while n>0:
        n//10
        count=count+1
n=num
ren=0
while num>0:
    r=num%10
    ren=ren+(r**count)
    n=n//10
