"""
Pattern 2:  1
            2 3
            4 5 6
            7 8 9 10
"""
n=int(input("Enter the number of row: "))
temp=1
for i in range(n):
    for j in range(i):
        print(temp,end="  ")
        temp+=1

    print()
