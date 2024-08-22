"""
Pattern 9:          * * * * *
                  * * * * *
                * * * * *
              * * * * *
            * * * * *
"""

n=int(input("Enter the size of Row:") )

for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(n):
        print("*",end=" ")
    print()
