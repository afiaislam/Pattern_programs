"""
Pattern 5:  * * * * * * * * *
            *               *
            *               *
            * * * * * * * * *
"""
m=int(input("Enter the size of Row: "))
n=int(input("Enter the size of Column: "))
for i in range(m):
    for j in range(n):
        if i==0 or j==0:
            print("*",end=" ")
        elif i==m-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()