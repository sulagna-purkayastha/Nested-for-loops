# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4
# 5
r=int(input("enter number"))
b=0
for i in range (r,0,-1):
    b+=1
    for j in range (1,i+1):
        print(b,end=" ")
    print("\r")    