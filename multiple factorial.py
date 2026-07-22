a=int(input("enter a number"))
b=int(input("enter a number"))
for i in range (a,b+1):
    fact=1
    for j in range (2,i+1):
            fact = fact*j
    print("factorial of ", i, "is", fact)  
