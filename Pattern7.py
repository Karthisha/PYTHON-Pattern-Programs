n=int(input("enter the number:"))
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    print("*"*(2*i-1),end="")
    print()
