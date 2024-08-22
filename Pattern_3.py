"""
Pattern 3:  1
            0 1
            1 0 1
            0 1 0 1
"""

n=int(input("Enter the row size: "))

for i in range(n):
    for j in range(i):
        if (i+j)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()