a=int(input("enter a number"))
THOR=0
for i in range(2,(a//2)+1):
    if a%i==0:
        THOR=1
if THOR==0:
    print(a, "is prime number")
else:
    print(a,"is composite")
