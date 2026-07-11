a=int(input("enter first range"))
b=int(input("enter second range"))
for i in range (a,b+1):
    for j in range (a , b+1):
        print(i,'x',j,'=', i*j)
    print(i,j)
