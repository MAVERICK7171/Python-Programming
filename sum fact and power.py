x=int(input("enter the value of x:"))
n=int(input("enter the value of n:"))
var=1
sum=0
for i in range(1,n+1):
     var=var*i
     sum=sum+(x**i)/var
     print("sum of the series is", var)



