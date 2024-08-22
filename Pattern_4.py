"""
Pattern 4:  5
            0 5
            5 0 5
            0 5 0 5
            5 0 5 0 5
"""

n=int(input("Enter the row size: "))

for i in range(n):
    for j in range(i):
        if (i+j)%2==0:
            print(5,end=" ")
        else:
            print(0,end=" ")
    print()