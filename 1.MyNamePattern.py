"""Enter any number
Then You can see my name, 
You can create functions for same code and utilize it whereever required!!"""
n=int(input())
mid=(n//2)
#This one is for pattern L
for i in range(1,n+1):
    print("*")
    if i==n:
       print("* "*(n))
print(" "*n)
#This one is for pattern A
for i in range(1,n+1):
    print(" "*(n-i),end="")
    if i==mid+1:
       if n%2==0:
           print("*"*(n+1),end="")
       else:
           print("*"*n,end="")
    else:
        print('*',end="")
        print("  "*(i-1),end="")
    print("*",end="")
    print()
print(" "*n) 
#This one is for pattern v
for i in range(1,n+1):
    print(" "*(i),end="")
    print("*",end="")
    print("  "*(n-i),end="")
    print("*",end="")
    print()
print(" "*n)
#This pattern is for A
for i in range(1,n+1):
    print(" "*(n-i),end="")
    if i==mid+1:
       if n%2==0:
           print("*"*(n+1),end="")
       else:
           print("*"*n,end="")
    else:
        print('*',end="")
        print("  "*(i-1),end="")
    print("*",end="")
    print()
print(" "*n)
#This one is for pattern N
for i in range(0,n):
    print(" "*mid,end="")
    print("*",end="")
    if i==0:
       print(" "*(n-1),end="")
    else:
       print(" "*(i-1),end="")
       print("*",end="")
       print(" "*(n-i-1),end="")
    print("*",end="")
    print()
print(" "*n)
#This one is for pattern Y
for i in range(1,n+1):
    print(" "*(i-1),end="")
    print("*",end="")
    print("  "*(n-i+1),end="")
    print("*",end="")
    print()
for i in range(n):
    print(" "*(n-2)," *")
print(" "*n)
#This pattern is for A
for i in range(1,n+1):
    print(" "*(n-i),end="")
    if i==mid+1:
       if n%2==0:
           print("*"*(n+1),end="")
       else:
           print("*"*n,end="")
    else:
        print('*',end="")
        print("  "*(i-1),end="")
    print("*",end="")
    print()
print()
print("LAVANYA@Patterns Lover!!!!")


