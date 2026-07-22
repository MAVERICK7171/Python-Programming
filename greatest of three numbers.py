a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a>b and a>c:
    print(a, 'is greatest')
elif b>a and b>c:
    print(b, 'is greatest')
elif c>a and c>a:
    print(c, 'is greatest')
else:
    print("number are equal")
