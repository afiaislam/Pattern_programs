"""
Pattern 6:  1 2 3 4 5
            A B C D
            1 2 3
            A B
            1
"""
n=int(input("Enter the size of row: "))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        if (i%2==0):
            b=chr(j+64)
            print(b,end=" ")  
        else:
            print(j,end=" ")

    print()