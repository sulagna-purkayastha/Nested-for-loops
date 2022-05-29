#    *
#   * *
#  * * *
# * * * *
#  * * * 
#   * * 
#    *
a=5
for i in range (1,a):
    b=a
    for b in range (i,b):
        print(" ",end="") 
    j=1
    for j in range (j,i):
        print("*",end=" ")
    print( )    
a=4
for i in range (0,a):
    j=0
    for c in range (j,i):
        print(" ",end="")
    for d in range (i,a):
        print("*",end=" ")
    print( )      