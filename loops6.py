#       *
#     * *
#   * * *
# * * * *
a=6
for i in range (1,a):
    b=a
    for b in range (i,b):
        print(" ",end=" ") 
    j=1
    for j in range (j,i):
        print("*",end=" ")
    print( )    