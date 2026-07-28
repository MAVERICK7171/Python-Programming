n=int(input("enter number of rows"))
for i in range(0,n):
      for j in range (0,n-i-1):
           print(' ',end='')
      for j in range (0,2*i+1):
          if j==0 or j==2*i :
              print("*", end="")
          else:
              print(' ', end='')
      print()
for i in range(1,n):
      for j in range(0,i):
           print(' ',end='')
      for j in range (0, 2*(n-i)-1):
            if j==0 or j==2*(n-i)-2:
                 print ("*", end='')
            else:
                  print(' ' , end='')
      print()
                      
