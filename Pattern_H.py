"""
Pattern 8:          *
                  * *
                * * *
              * * * *
            * * * * *
"""
n=int(input("Enter the size of Row: "))

for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()