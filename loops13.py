a=8
for i in range (0,a+1,2):
    b=a
    for b in range (i,b):
        print(" ",end="")
    j=1
    for j in range (j,i):
        print("*",end=" ")
    print( )  